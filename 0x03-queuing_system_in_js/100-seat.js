import { promisify } from "util";
import { createClient } from "redis";
import { createQueue } from "kue";

const express = require('express');
const app = express();

const client = createClient();
const getAsync = promisify(client.get).bind(client);
let reservationEnabled = true;
const queue = createQueue();

client.on('connect', () => {
    console.log('Redis client connected to the server');
  });
  
  client.on('error', (err) => {
    console.error('Redis client not connected to the server:', err);
  });

function reserveSeat(number) {
  client.set('available_seats', number);
}

reserveSeat(50);
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats;
}

app.get('/available_seats', async (request, response) => {
  const available_seats = await getCurrentAvailableSeats();
  response.json({ "numberOfAvailableSeats": available_seats });
});

app.get('/reserve_seat', (request, response) => {
  if (reservationEnabled) {
    const job = queue.create('reserve_seat').save((err) => {
      if (err) {
        response.json({"status": "Reservation failed"});
        return;
      } else {
          response.json({"status": "Reservation in process"});
          job.on('complete', () => {
            console.log(`Seat reservation job ${job.id} completed`);
          });
          job.on('failed', (error) => {
            console.log(`Seat reservation job ${job.id} failed: ${error}`);
          });
        }
    });
  } else {
    response.json({ status: 'Reservation are blocked' });
  }
});

app.get('/process', (request, response) => {
    response.json({"status": "Queue processing"});
    queue.process('reserve_seat', async (job, done) => {
      const seat = Number(await getCurrentAvailableSeats());
      if (seat === 0) {
	    reservationEnabled = false;
	    done(Error('Not enough seats available'));
	  } else {
	      reserveSeat(seat - 1);
	      done();
	  }
    });
});

const port = 1245;

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});