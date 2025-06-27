DO
$$
DECLARE
    work_date DATE := DATE '2025-06-01';
    end_date  DATE := DATE '2025-12-31';
BEGIN
    WHILE work_date <= end_date LOOP
        -- Skip weekends: Friday(5), Saturday(6)
        IF EXTRACT(DOW FROM work_date) NOT IN (5, 6) THEN
            INSERT INTO work_days (date, day_name, is_holiday, description)
            VALUES (
                work_date,
                to_char(work_date, 'FMDay'),          -- <-- day name
                CASE work_date
                    
                    WHEN DATE '2025-06-05' THEN TRUE  -- Arafat Tite
                    WHEN DATE '2025-06-08' THEN TRUE  -- Eid El-Adha
                    WHEN DATE '2025-06-09' THEN TRUE  -- Eid EL-Adha
                    WHEN DATE '2025-06-26' THEN TRUE  -- Hijri New Year (observed)
                    WHEN DATE '2025-07-03' THEN TRUE  -- 30 June Revolution (observed)
                    WHEN DATE '2025-07-24' THEN TRUE  -- 23 July Revolution
                    WHEN DATE '2025-09-04' THEN TRUE  -- Prophet's Day
                    WHEN DATE '2025-10-09' THEN TRUE  -- Armed Forces Day
                    ELSE FALSE
                END,
                CASE work_date
                    WHEN DATE '2025-06-05' THEN 'Arafat Tite'
                    WHEN DATE '2025-06-08' THEN 'Eid El-Adha'
                    WHEN DATE '2025-06-09' THEN 'Eid EL-Adha'
                    WHEN DATE '2025-06-26' THEN 'Hijri New Year (observed)'
                    WHEN DATE '2025-07-03' THEN '30 June Revolution Day'
                    WHEN DATE '2025-07-24' THEN '23rd July Revolution Day'
                    WHEN DATE '2025-09-04' THEN 'Prophet''s Day'
                    WHEN DATE '2025-10-09' THEN 'Armed Forces Day'
                    ELSE NULL
                END
            );
        END IF;

        work_date := work_date + 1;   -- next day
    END LOOP;
END
$$;