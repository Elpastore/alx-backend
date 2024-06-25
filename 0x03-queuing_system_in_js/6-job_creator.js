import { createQueue } from 'kue';

const queue = createQueue();

const jobObj = {
  'phoneNumber': '23424285482',
  'message': 'Text message to be display  as a test'
}

const job = queue.create('push_notification_code', jobObj).save(err => {
  if(err) {
    console.error('error: ', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});