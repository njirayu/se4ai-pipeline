# Reflection

Name: Natthakit Jirayuthanyawat

Answer each question in 2–3 sentences.

**1. Which antipatterns from the lecture did `train_all.py` show? Point to the lines.**

> It is a monolithic script: load, clean, features, train, evaluate and save all share one global `df`, so no stage can be tested or reused alone. It has hard-coded values that should be parameters: the file name, the date format and the tree depth. It also keeps dead experimental code (the `USE_LOG_PRICE` block, lines 27–31), and it is run by hand once a year with no tests and no evaluation gate before the model is saved.

**2. Suppose there were no test and no evaluation gate. What would have happened when the 2026 batch arrived? Think about both the crash and the missing `sqft` values.**

> The date crash is actually good for this, since it serves as a notice. But a quick "fix" such as `errors="coerce"` would silently turn the new dates into missing values, and the tree model would train on the 12 rows with missing `sqft` without any error. The result would be a worse model saved and shown to users as "fair value", and without the gate even a really bad model would be saved with nobody noticing.

**3. In the real marketplace, which non-ML parts of the system should trigger this pipeline or feed it data?**

> The sales or transaction system should feed it: each export of closed sales (like the 2026 Q1 file) should trigger a run, or a scheduler should start it regularly (for example, monthly). The listings database and data warehouse provide the home attributes. Monitoring of the live site should also trigger retraining when the gap between predicted values and actual sale prices grows, and the website's deployment step should only pick up a model that passed the gate.
