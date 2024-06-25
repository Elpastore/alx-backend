const { describe, it, before, after, afterEach } = require('mocha');
const assert = require('assert');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job.js');

const queue = kue.createQueue();

describe('Test createPushNotificationsJobs function', function() {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', function() {
    assert.throws(() => createPushNotificationsJobs('job', queue), { message: 'Jobs is not an array' });
  });

  it('should test whether jobs are created', function() {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    assert.strictEqual(queue.testMode.jobs.length, 2);

    assert.strictEqual(queue.testMode.jobs[0].type, 'push_notification_code_3');
    assert.deepStrictEqual(queue.testMode.jobs[0].data, jobs[0]);

    assert.strictEqual(queue.testMode.jobs[1].type, 'push_notification_code_3');
    assert.deepStrictEqual(queue.testMode.jobs[1].data, jobs[1]);
  });
});
