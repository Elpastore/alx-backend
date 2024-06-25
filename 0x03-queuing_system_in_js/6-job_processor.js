import { createQueue } from "kue";
const queue = createQueue();


function sendNotification(phoneNumber, messsage) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${messsage}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});