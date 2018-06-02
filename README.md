# Demo REST API with SQLAlchemy flask postgres and unit testing.

## Academy

The idea is one Academy API with some basic requirements.

Use cases implemented:

*   There are Teachers.
*   There are Students.
*   Students are in classes that teachers teach.
*   Teachers can create multiple quizzes with many questions (each question is multiple choice) Teachers can assign quizzes to students.
*   Students solve/answer questions to complete the quiz, but they don't have to complete it at once. (Partial submissions can be made).
*   Quizzes need to get graded.
*   For each teacher, they can calculate each student's total grade accumulated over a semester for their classes.

To run the app first start a database postgres with docker:
1.   `docker pull postgres`
2.   `docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

All the Tables will be created if not exits.


Note: Python version 3.6 was used.


Do not hesitate to give me a star or just follow me.

I hope you like it.
