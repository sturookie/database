# database
2021 Database

Here are some instructions for our application. This is a database query application that allows users to search for information around all colleges in New York State. The information includes outdoor sports, diet, crime and other useful information for college students. The app also allows users to learn more about universities, including their majors.


First step: Run load_data.py to preprocess the data from the four datasets and pass it into your own database. Because of the different sources of our four data sets and the different formats of the data, a lot of data cleaning is required without data loss. In addition, to avoid data redundancy, we need to normalize and split the data from the master data set, which requires more data preprocessing.

Some explanation for schema: After we normalized the information in the master data set, we transformed it into four different tables, which recorded the main information of the university, the geographical location of the university, the major of the university and other information. Operations such as modifying the database after processing will not cause errors or major changes.

Second step: Run app.py to connect to the database and integrate functionality. After running, the terminal interface will generate a website, click the website will enter the interface. After that, users can explore information about the university and its surroundings at will. The final result of the query is stored in the JSON format, which can be further utilized by users after use. Json files are stored in a way that makes the subsequent use of query results more efficient and fast, because it does not require a series of complex operations again. This is also a non-relational way of storing data.
