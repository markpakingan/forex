### Conceptual Exercise

Answer the following questions below:

-   What are important differences between Python and JavaScript?
<!--
Python is used on server side (backend) while JS is for client side (front end).
You need to an interpreter to run Python. JS is built in in most websites.
Python is encoded using ASCII. On the other hard HS has the UTF-encoding. -->

-   Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
    <!-- can try to get a missing key (like "c") *without* your programming
    crashing. -->

-   What is a unit test?
      <!-- Unit test is a simple way (usually narrow) way of testing a code. This works well with function. -->

-   What is an integration test?

    <!-- Integration testing is a broader way of testing your code. It checks if multiple modules are working together. It also tests impure functions with side effect.  -->

-   What is the role of web application framework, like Flask?
<!-- 
Flask is a web frameworks the provides request and response functions. 
It provides functionalities like:
-   handle web requests
-   produce dynamic HTML
-   handle forms and cookies
-   connect databases -->

-   You can pass information to Flask either as a parameter in a route URL
    (like '/foods/pretzel') or using a URL query param (like
    'foods?type=pretzel'). How might you choose which one is a better fit
    for an application?

<!-- - Path parameters are used to identify specific resource(s). The values can't be ommited. On the other hand, query params are used to sort/filter resources -->

-   How do you collect data from a URL placeholder parameter using Flask?
<!--   
  You can collect data from a URL placeholder parameter by defining a route with a placeholder in the URL and then accessing the placeholder value in the corresponding function using the request object. -->

-   How do you collect data from the query string using Flask?
<!-- You can use the "request" object to access the data. 
You can use the "request.args" attribute to access the data from the query string -->


-   How do you collect data from the body of the request using Flask?
 <!-- you can access the data in the body of a request using the request object. The request.data attribute returns the raw data in the body of the request -->

 

-   What is a cookie and what kinds of things are they commonly used for?

<!-- Cookies are small text data sent to your browser by a website you visit. it also can be a username and pww that are used to identify your computer when using a computer network -->

-   What is the session object in Flask?
<!--
This is a dictionary object that contains key value pairs for session variables and associated values. -->

-   What does Flask's `jsonify()` do?
<!-- jsonify() function returns a Response object. Flask serializes your data as JSON and adds it to this Response object. -->
