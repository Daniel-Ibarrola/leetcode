# API Design

## REST

**REST** stands for **RE**presentational **S**tate **T**ransfer. It is not a protocol or a standard, but an **architectural style** for designing networked applications. A web service or API that follows the principles of REST is called a **RESTful** API.

The core idea of REST is to build APIs on top of the existing, proven technology of the web: the HTTP protocol. Instead of inventing a new set of rules for how a client and server should communicate, REST leverages the standard methods and concepts of HTTP.

---

### Key Principles of REST

To be considered RESTful, an architecture must adhere to several constraints:

1.  **Client-Server Architecture:** The client (e.g., a web browser or mobile app) is responsible for the user interface, while the server is responsible for storing and retrieving data. They are separate concerns and evolve independently.

2.  **Statelessness:** This is a crucial constraint. Every request from a client to a server must contain all the information the server needs to understand and fulfill that request. The server does not store any information about the client's state between requests. If a client state is needed (like being logged in), the client is responsible for sending it with every request (e.g., as an authentication token).

3.  **Cacheability:** Responses from the server should be defined as cacheable or not. This allows clients and intermediaries (like Content Delivery Networks) to store a copy of the response, improving performance and scalability.

4.  **Uniform Interface:** This is the fundamental design principle of REST and simplifies the architecture. It has four sub-constraints:
    *   **Resource-Based:** Everything is a "resource." A resource can be a user, a product, an order—any object of data. Resources are identified by a unique URI (Uniform Resource Identifier), like `/users/123`.
    *   **Manipulation of Resources Through Representations:** The client doesn't get the resource itself; it gets a *representation* of the resource (e.g., a JSON or XML object). The client uses this representation to modify the resource's state on the server.
    *   **Self-Descriptive Messages:** Each request is self-contained. For example, a request specifies that it wants a `application/json` representation, and the response uses a status code like `200 OK` or `404 Not Found` to communicate the outcome.
    *   **HATEOAS (Hypermedia as the Engine of Application State):** A RESTful client should be able to navigate the entire API just by following links provided in the responses from the server. For example, a response for a user might contain a link to view that user's orders.

---

### Main HTTP Verbs (HTTP Methods)

REST uses standard HTTP verbs to perform actions on resources. The most common ones are:

| Verb    | Action                             | Description                                                                                                                              | Idempotent? |
| :------ | :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| **GET**     | **Read** a resource                | Retrieves a representation of a resource. This is a safe operation, meaning it doesn't change the resource's state.                      | Yes         |
| **POST**    | **Create** a new resource          | Submits data to be processed to create a new resource. Typically used when the client doesn't know the URI of the new resource beforehand. | No          |
| **PUT**     | **Update/Replace** a resource      | Replaces an existing resource with a new representation. The entire resource must be sent in the request.                                | Yes         |
| **DELETE**  | **Delete** a resource              | Removes a specific resource.                                                                                                             | Yes         |
| **PATCH**   | **Partially Update** a resource    | Applies a partial modification to a resource. Unlike `PUT`, you only need to send the data for the fields you want to change.              | No          |

**What does Idempotent mean?**
An operation is **idempotent** if making the same request multiple times has the same effect as making it once.
*   `GET /users/123` will always return the same user data (safe and idempotent).
*   `DELETE /users/123` will delete the user the first time, and subsequent calls will result in "Not Found," but the state of the system remains the same (user is deleted). So, it's idempotent.
*   `POST /users` will create a new user *every time* you call it. This is **not** idempotent.

#### Example Usage:

Let's imagine a REST API for managing a collection of `articles`.

*   `GET /articles`: Get a list of all articles.
*   `GET /articles/42`: Get the article with ID 42.
*   `POST /articles`: Create a new article. The request body would contain the new article's data (e.g., title, content).
*   `PUT /articles/42`: Completely replace article 42 with the data in the request body.
*   `PATCH /articles/42`: Update just the title of article 42. The request body might just be `{"title": "A New Title"}`.
*   `DELETE /articles/42`: Delete the article with ID 42.
Of course. This is a fundamental concept in software design, and here is a clear explanation suitable for your guide.