-- Remove existing June and July 2025 data for user 1
DELETE FROM attendance
WHERE user_id = 1
  AND date BETWEEN '2025-06-01' AND '2025-07-31';

-- Insert June attendance records
INSERT INTO attendance (user_id, date, status) VALUES
  -- Week 1 (June)
  (1, '2025-06-02', 'onsite'),
  (1, '2025-06-03', 'remote'),
  (1, '2025-06-04', 'onsite'),
  (1, '2025-06-05', 'leave'),
  (1, '2025-06-06', 'night'),

  -- Week 2
  (1, '2025-06-09', 'onsite'),
  (1, '2025-06-10', 'remote'),
  (1, '2025-06-11', 'onsite'),
  (1, '2025-06-12', 'night'),
  (1, '2025-06-13', 'remote'),

  -- Week 3
  (1, '2025-06-16', 'onsite'),
  (1, '2025-06-17', 'remote'),
  (1, '2025-06-18', 'leave'),
  (1, '2025-06-19', 'onsite'),
  (1, '2025-06-20', 'night'),

  -- Week 4
  (1, '2025-06-23', 'onsite'),
  (1, '2025-06-24', 'remote'),
  (1, '2025-06-25', 'onsite'),
  (1, '2025-06-26', 'leave'),
  (1, '2025-06-27', 'night');

-- Insert July attendance records
INSERT INTO attendance (user_id, date, status) VALUES
  -- Week 1 (July)
  (1, '2025-07-01', 'onsite'),
  (1, '2025-07-02', 'remote'),

  -- Week 2
  (1, '2025-07-06', 'onsite'),
  (1, '2025-07-07', 'remote'),
  (1, '2025-07-08', 'night'),
  (1, '2025-07-09', 'onsite'),
  (1, '2025-07-10', 'onsite'),

  -- Week 3
  (1, '2025-07-13', 'remote'),
  (1, '2025-07-14', 'onsite'),
  (1, '2025-07-15', 'night'),
  (1, '2025-07-16', 'onsite'),
  (1, '2025-07-17', 'remote'),

  -- Week 4
  (1, '2025-07-20', 'leave'),
  (1, '2025-07-21', 'onsite'),
  (1, '2025-07-22', 'onsite'),
  (1, '2025-07-23', 'remote'),

  -- Week 5
  (1, '2025-07-27', 'onsite'),
  (1, '2025-07-28', 'night'),
  (1, '2025-07-29', 'remote'),
  (1, '2025-07-30', 'onsite'),
  (1, '2025-07-31', 'onsite');