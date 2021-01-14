### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  - some include:
    - Python variables not needing to be declared with var, const or let
    - syntax situations that would have returned undefined in JS, raise an error in Python
    - Python functions can't be chained as easily as JS functions
    - Python has function that are more powerful/featureful than their JS counterparts
    - JS destructuring is not present in Python
    - Python has a very descriptive help library, including custom functions
    - All Python string need explicit quotation marks when it is used as a key in a key value pair, unlike in JS where quotation marks can be skipped
    - Python dot notation is reserved for attributes and methods in OOP, unlike in JS where they can be used for accessing methods in dictionaries/objects as well
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
    `dic = {"a": 1, "b": 2}`
    `dic.get('c')` # returns `None`
    `'c' in dic` # returns `False`
- What is a unit test?
    - Tests a single unit/function/module of code. Focuses on input and output. Often simpler to test, and can give help narrow down issues while debugging apps.
- What is an integration test?
    - Tests the whole path as seen by the user, involving several functions, modules. Ensures user sees/receives the correct output. Can be more challenging to test, and might involve using a mock server and mock requests. Can be difficult to rely on fully, for finding a small bug, since it's scope is broader.
- What is the role of web application framework, like Flask?
    - It is meant to aid in the faster/more efficient development of web applications by helping manage resources, routes, and resources.
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    - Using RESTful API conventions, it is can be a better fit to use resources like '/foods/pretzel' when they need to be hardcoded and require custom or extended treatment. For parameters that will vary and require flexibility, query parameters are much more convenient.
- How do you collect data from a URL placeholder parameter using Flask?
    `app.route("/<username>"")`
    `def retrieve(username):`  
    `# use variable username`
- How do you collect data from the query string using Flask?
    `variable = request.args['variable']`
- How do you collect data from the body of the request using Flask?
    `variable = request.form['variable']`
- What is a cookie and what kinds of things are they commonly used for?
    - Cookies are string key:value pairs that are stored in the browser to save some sort of state. It is sent to the server with each request. The type and amount of data that can be stored is very limited. Cookie data is not private.
- What is the session object in Flask?
    - A dictionary-like object which is accessible throughout the app, and preserves the type of data stored in it. It is not human readable, but instead serialized, "signed" for security authentification, but is not meant to be private. It lasts as long as the browser stays open.
- What does Flask's `jsonify()` do?
    - It converts data to JSON, for easy transport and parsing of complex data out of the server to a browser or application.