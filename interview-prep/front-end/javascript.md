# JavaScript Questions

**What is a closure?**

A closure is the combination of a function bundled together (enclosed) with references to its surrounding state
(the lexical environment). In JavaScript, closures are created every time a function is created, at function creation time.
It allows an inner function to access the scope of an outer function even after the outer function has finished executing.
Example:
```javascript
function outer() {
  const name = "Mozilla";
  function inner() {
    console.log(name);
  }
  return inner;
}
const myFunc = outer();
myFunc(); // Logs: "Mozilla"
```

---

**What is the event loop?**

The event loop is a mechanism that allows JavaScript to perform non-blocking I/O operations despite being single-threaded.
It constantly monitors the Call Stack and the Callback Queue. If the Call Stack is empty, it takes the first task from the queue and pushes
it onto the stack, effectively executing it.

---

**What's the difference between var, let, and const?**

- `var`: Function-scoped, can be re-declared and updated, hoisted with `undefined` initialization.
- `let`: Block-scoped, can be updated but not re-declared in the same scope, hoisted but in the Temporal Dead Zone (TDZ).
- `const`: Block-scoped, cannot be updated or re-declared (must be initialized at declaration), hoisted but in the TDZ.

```javascript
{
  var x = 1;
  let y = 2;
  const z = 3;
}
console.log(x); // 1
console.log(y); // ReferenceError
```

---

**What is hoisting?**

Hoisting is JavaScript's default behavior of moving declarations to the top of the current scope.
Variable declarations (`var`) and function declarations are hoisted. `let` and `const` are also hoisted but
remain uninitialized in the TDZ until the code execution reaches their declaration.

```javascript
console.log(a); // undefined
var a = 5;

console.log(b); // ReferenceError
let b = 10;
```

---

**What is the difference between == and ===?**

- `==` (Abstract Equality): Performs type coercion before comparing the values.
- `===` (Strict Equality): Compares both value and type without coercion.

```javascript
5 == "5"  // true
5 === "5" // false
```

---

**What is a promise?**

A Promise is an object representing the eventual completion (or failure) of an asynchronous operation and its resulting value.
It can be in one of three states: pending, fulfilled, or rejected.

```javascript
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Success!"), 1000);
});
```

---

**How do async / await work?**

`async` and `await` are syntactic sugar built on top of Promises.
`async` functions always return a promise.
`await` pauses the execution of the async function until the promise is settled,
making asynchronous code look and behave more like synchronous code.

```javascript
async function fetchData() {
  const response = await fetch("https://api.example.com");
  const data = await response.json();
  return data;
}
```

---

**What is `this` in JavaScript?**

The value of `this` depends on how a function is called (the call site).
In a method, it refers to the owner object.
Alone, it refers to the global object. In a function (strict mode), it is `undefined`.
In an event, it refers to the element that received the event. Arrow functions do not have their own `this`;
they inherit it from the parent lexical scope.

```javascript
const obj = {
  prop: 42,
  func: function() { return this.prop; }
};
console.log(obj.func()); // 42
```

---

**What is prototypal inheritance?**

JavaScript uses prototypal inheritance, where objects can inherit properties and methods
from other objects via a prototype chain. Every object has a private property which holds a
link to another object called its prototype.

```javascript
const animal = { eats: true };
const rabbit = Object.create(animal);
console.log(rabbit.eats); // true
```

---

**What's the difference between synchronous and asynchronous code?**

- Synchronous code: Executed line by line, each operation must finish before the next one starts (blocking).
- Asynchronous code: Allows operations to run in the background, letting the main thread continue executing other code (non-blocking).

---

**What are higher-order functions?**

Higher-order functions are functions that take one or more functions as
arguments or return a function as their result. Examples include `map`, `filter`, and `reduce`.

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // [2, 4, 6]
```

---

**What is destructuring?**

Destructuring assignment is a syntax that allows unpacking values from arrays or properties from objects into distinct variables.

```javascript
const user = { id: 1, name: "Alice" };
const { id, name } = user;
```

---

**What are spread and rest operators?**

Both use the `...` syntax:
- Spread operator: Expands an iterable (like an array or object) into individual elements or properties.
- Rest operator: Collects multiple elements into a single array or object (often used in function parameters).

```javascript
// Spread
const arr = [1, 2, ...[3, 4]]; // [1, 2, 3, 4]
// Rest
function sum(...args) { return args.length; }
```

---

**What is the difference between null and undefined?**

- `undefined`: Means a variable has been declared but has not yet been assigned a value.
- `null`: Is an assignment value that represents the intentional absence of any object value.

```javascript
let a;
console.log(a); // undefined
let b = null;
console.log(b); // null
```

---

**What is the difference between call, apply, and bind?**

All three explicitly set the value of `this` for a function.
- `call`: invokes the function immediately, arguments passed individually.
- `apply`: invokes the function immediately, arguments passed as an array.
- `bind`: returns a *new* function with `this` permanently bound — does not invoke immediately.

```javascript
function greet(greeting, punct) {
  return `${greeting}, ${this.name}${punct}`;
}
const user = { name: "Alice" };

greet.call(user, "Hello", "!");   // "Hello, Alice!"
greet.apply(user, ["Hi", "."]);   // "Hi, Alice."
const sayHi = greet.bind(user, "Hey");
sayHi("?");                        // "Hey, Alice?"
```

---

**What is debouncing? What is throttling?**

Both limit how often a function executes in response to rapid events.

- **Debounce**: delays execution until the event *stops* firing for a given wait period. Good for search-as-you-type (fire only after the user pauses).
- **Throttle**: guarantees the function fires *at most once* per interval, regardless of how often the event fires. Good for scroll/resize handlers.

```javascript
// Debounce — fires 300ms after the last call
function debounce(fn, wait) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), wait);
  };
}

// Throttle — fires at most once per 300ms
function throttle(fn, limit) {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= limit) {
      lastCall = now;
      fn(...args);
    }
  };
}
```

---

**What are microtasks vs macrotasks?**

The event loop processes tasks in two queues:

- **Macrotask queue** (task queue): `setTimeout`, `setInterval`, I/O callbacks. One macrotask is dequeued per event loop tick.
- **Microtask queue**: Promise callbacks (`.then`, `.catch`), `queueMicrotask`, `MutationObserver`. The *entire* microtask queue is drained after every macrotask — before the next macrotask or render.

```javascript
console.log("1 — sync");

setTimeout(() => console.log("2 — macrotask"), 0);

Promise.resolve().then(() => console.log("3 — microtask"));

console.log("4 — sync");

// Output order: 1, 4, 3, 2
```

---

**What is optional chaining (?.) and nullish coalescing (??)?**

- `?.` short-circuits and returns `undefined` if the left side is `null` or `undefined`, instead of throwing.
- `??` returns the right-hand value only when the left side is `null` or `undefined` (unlike `||`, which also triggers on `0`, `""`, `false`).

```javascript
const user = { address: null };

console.log(user.address?.city);          // undefined (no error)
console.log(user.address?.city ?? "N/A"); // "N/A"

// ?? vs ||
const count = 0;
console.log(count || 10);  // 10  (0 is falsy)
console.log(count ?? 10);  // 0   (0 is not null/undefined)
```

---

**When should you use Map over Object, and Set over Array?**

- **Map vs Object**: Use `Map` when keys are non-strings, insertion order matters, or you need `.size`. Objects are fine for plain record shapes with string keys.
- **Set vs Array**: Use `Set` when you need guaranteed uniqueness and O(1) `.has()`. Arrays are ordered lists that can contain duplicates.

```javascript
const map = new Map();
map.set({ id: 1 }, "value"); // object as key — not possible with plain object

const set = new Set([1, 2, 2, 3]); // {1, 2, 3}
set.has(2); // true — O(1)
```

---

**What is event bubbling, capturing, and delegation?**

- **Bubbling**: an event fires on the target element, then propagates *up* through ancestors (default behavior).
- **Capturing**: the event travels *down* from the root to the target before bubbling back up. Use `addEventListener(event, fn, true)` to listen in the capture phase.
- **Delegation**: attach a single listener on a parent instead of many listeners on children. Relies on bubbling to catch events from any descendant.

```javascript
// Delegation — one listener handles all <li> clicks
document.querySelector("ul").addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    console.log("Clicked:", e.target.textContent);
  }
});
```

`e.stopPropagation()` halts further propagation. `e.preventDefault()` prevents the default browser action (e.g., form submission).

---

**What is an IIFE?**

An Immediately Invoked Function Expression — a function that is defined and called at the same time. Used to create a private scope and avoid polluting the global namespace (common pre-ES6 modules pattern).

```javascript
(function () {
  const private = "not visible outside";
  console.log(private);
})();
```

---

**What is memoization?**

Memoization is an optimization technique that caches the result of a function call so that subsequent calls with the same arguments return the cached value instead of recomputing.

```javascript
function memoize(fn) {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) return cache.get(key);
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

const factorial = memoize((n) => (n <= 1 ? 1 : n * factorial(n - 1)));
```

---

**What is currying?**

Currying transforms a function that takes multiple arguments into a sequence of functions each taking one argument.

```javascript
// Normal
const add = (a, b) => a + b;

// Curried
const curriedAdd = (a) => (b) => a + b;
const add5 = curriedAdd(5);
add5(3); // 8
add5(10); // 15
```

Useful for partial application — pre-filling some arguments to create reusable specialized functions.

---

**How does garbage collection work in JavaScript?**

JavaScript uses *mark-and-sweep*: the GC periodically marks all values reachable from the root (global scope, call stack), then sweeps (frees) anything unremarked. A value is collected once there are no more references to it.

Common memory leak sources:
- Forgotten `setInterval` / event listeners holding references
- Closures capturing large objects unnecessarily
- Global variables accumulating state

`WeakMap` and `WeakSet` hold *weak* references — they don't prevent GC of their keys/values, making them useful for caches keyed to objects.

```javascript
let cache = new WeakMap();
let obj = {};
cache.set(obj, "data");
obj = null; // obj can now be garbage collected; cache entry disappears
```
