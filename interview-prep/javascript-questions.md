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

**What is the event loop?**

The event loop is a mechanism that allows JavaScript to perform non-blocking I/O operations despite being single-threaded.
It constantly monitors the Call Stack and the Callback Queue. If the Call Stack is empty, it takes the first task from the queue and pushes
it onto the stack, effectively executing it.

**What’s the difference between var, let, and const?**

- `var`: Function-scoped, can be re-declared and updated, hoisted with `undefined` initialization.
- `let`: Block-scoped, can be updated but not re-declared in the same scope, hoisted but in the Temporal Dead Zone (TDZ).
- `const`: Block-scoped, cannot be updated or re-declared (must be initialized at declaration), hoisted but in the TDZ.
Example:
```javascript
{
  var x = 1;
  let y = 2;
  const z = 3;
}
console.log(x); // 1
console.log(y); // ReferenceError
```

**What is hoisting?**

Hoisting is JavaScript's default behavior of moving declarations to the top of the current scope. 
Variable declarations (`var`) and function declarations are hoisted. `let` and `const` are also hoisted but 
remain uninitialized in the TDZ until the code execution reaches their declaration.
Example:
```javascript
console.log(a); // undefined
var a = 5;

console.log(b); // ReferenceError
let b = 10;
```

**What is the difference between == and ===?**
- `==` (Abstract Equality): Performs type coercion before comparing the values.
- `===` (Strict Equality): Compares both value and type without coercion.
Example:
```javascript
5 == "5"  // true
5 === "5" // false
```

**What is a promise?**

A Promise is an object representing the eventual completion (or failure) of an asynchronous operation and its resulting value. 
It can be in one of three states: pending, fulfilled, or rejected.
Example:
```javascript
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Success!"), 1000);
});
```

**How do async / await work?**

`async` and `await` are syntactic sugar built on top of Promises.
`async` functions always return a promise. 
`await` pauses the execution of the async function until the promise is settled, 
making asynchronous code look and behave more like synchronous code.
Example:
```javascript
async function fetchData() {
  const response = await fetch("https://api.example.com");
  const data = await response.json();
  return data;
}
```

**What is this in JavaScript?**
The value of `this` depends on how a function is called (the call site). 
In a method, it refers to the owner object. 
Alone, it refers to the global object. In a function (strict mode), it is `undefined`. 
In an event, it refers to the element that received the event. Arrow functions do not have their own `this`;
they inherit it from the parent lexical scope.
Example:
```javascript
const obj = {
  prop: 42,
  func: function() { return this.prop; }
};
console.log(obj.func()); // 42
```

**What is prototypal inheritance?**
JavaScript uses prototypal inheritance, where objects can inherit properties and methods 
from other objects via a prototype chain. Every object has a private property which holds a 
link to another object called its prototype.
Example:
```javascript
const animal = { eats: true };
const rabbit = Object.create(animal);
console.log(rabbit.eats); // true
```

**What’s the difference between synchronous and asynchronous code?**
- Synchronous code: Executed line by line, each operation must finish before the next one starts (blocking).
- Asynchronous code: Allows operations to run in the background, letting the main thread continue executing other code (non-blocking).

**What are higher-order functions?**
Higher-order functions are functions that take one or more functions as
arguments or return a function as their result. Examples include `map`, `filter`, and `reduce`.
Example:
```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // [2, 4, 6]
```

**What is destructuring?**
Destructuring assignment is a syntax that allows unpacking values from arrays or properties from objects into distinct variables.
Example:
```javascript
const user = { id: 1, name: "Alice" };
const { id, name } = user;
```

**What are spread and rest operators?**
Both use the `...` syntax:
- Spread operator: Expands an iterable (like an array or object) into individual elements or properties.
- Rest operator: Collects multiple elements into a single array or object (often used in function parameters).
Example:
```javascript
// Spread
const arr = [1, 2, ...[3, 4]]; // [1, 2, 3, 4]
// Rest
function sum(...args) { return args.length; }
```

**What is the difference between null and undefined?**
- `undefined`: Means a variable has been declared but has not yet been assigned a value.
- `null`: Is an assignment value that represents the intentional absence of any object value.
Example:
```javascript
let a;
console.log(a); // undefined
let b = null;
console.log(b); // null
```

## Typescript Questions

**What is the difference between type and interface?**
- `interface`: Primarily for defining object shapes. 
Supports declaration merging (you can define the same interface multiple times and they will merge).
- `type`: Can define objects but also primitives, unions, tuples, and intersections. 
Does not support declaration merging.
Example:
```typescript
interface User { name: string; }
type ID = number | string;
```

**What are union and intersection types?**
- Union (`|`): Allows a value to be one of several types (e.g., `string | number`).
- Intersection (`&`): Combines multiple types into one, requiring the value to satisfy all combined types.
Example:
```typescript
type Status = "success" | "error";
type AdminUser = User & { role: string };
```

**What is type narrowing?**
Type narrowing is the process of refining a type from a broader type to a more specific
type using conditional checks (e.g., `typeof`, `instanceof`, or truthiness checks).
Example:
```typescript
function print(val: string | number) {
  if (typeof val === "string") {
    console.log(val.toUpperCase()); // Narrowed to string
  }
}
```

**What is a type guard?**
A type guard is an expression that performs a runtime check to guarantee the type in some scope.
It can be a simple `typeof` check or a custom function using the `is` keyword (Type Predicate).
Example:
```typescript
function isString(val: any): val is string {
  return typeof val === "string";
}
```

**What is unknown vs any?**
- `any`: Opts out of type checking entirely. You can do anything with an `any` type.
- `unknown`: The type-safe counterpart of `any`. You can assign anything to `unknown`, 
but you cannot perform operations on it without first narrowing the type.
Example:
```typescript
let val: unknown = "Hello";
// val.toUpperCase(); // Error
if (typeof val === "string") val.toUpperCase(); // OK
```

**What is structural typing?**
TypeScript uses a structural type system (also called duck typing). 
If two types have the same shape (the same members), they are considered compatible, regardless of their explicit declarations.
Example:
```typescript
interface Point { x: number; y: number; }
const p: Point = { x: 10, y: 20, z: 30 }; // OK, has required members
```

**What is an enum, and should you use it?**
Enums allow defining a set of named constants. While they provide clarity, they can have pitfalls
(like numeric enums being not fully type-safe or increasing bundle size). 
Many developers prefer `const object` or union types of string literals instead.
Example:
```typescript
enum Color { Red, Green, Blue }
let c: Color = Color.Green;
```

**What are optional and readonly properties?**
- Optional (`?`): Properties that may or may not be present on an object.
- `readonly`: Properties that cannot be modified after the object is initialized.
Example:
```typescript
interface Car {
  readonly brand: string;
  model?: string;
}
```

**What is never used for?**
The `never` type represents the type of values that never occur. 
It's used for functions that always throw an error, infinite loops, or to handle "impossible" cases in exhaustive type checking.

Example:
```typescript
function throwError(msg: string): never {
  throw new Error(msg);
}
```

**What’s the difference between compile-time and runtime types?**
Compile-time types exist only during TypeScript compilation for type checking and are removed (erased)
during the transpilation to JavaScript. Runtime types are the actual types of values as they exist 
when the code is executed in the browser or Node.js.
Example:
```typescript
// TS: let x: number = 5;
// JS: let x = 5; (type information is gone)
```

## React Questions

**What is React and how does it work?**
React is a JavaScript library for building user interfaces. 
It works by creating a virtual representation of the UI (Virtual DOM) and efficiently 
updating the actual DOM only where changes have occurred using a process called reconciliation.


**What is the virtual DOM?**
The Virtual DOM is a lightweight copy of the actual DOM kept in memory.
React uses it to calculate the minimal number of changes needed to update the UI, 
improving performance by avoiding expensive direct DOM manipulations.
Example:
When a component's state changes, React creates a new Virtual DOM tree and compares it with the previous one (diffing).

**What is the difference between props and state?**
- `props`: Short for properties, passed from parent to child components. They are read-only (immutable) from the child's perspective.
- `state`: Managed within the component itself. It is mutable (via setter functions) and triggers a re-render when it changes.
Example:
```jsx
function Welcome(props) {
  const [count, setCount] = useState(0); // State
  return <h1>Hello, {props.name}</h1>; // Props
}
```

**What are hooks?**
Hooks are functions that let you "hook into" React state and lifecycle features from function components.
Examples include `useState`, `useEffect`, and `useContext`.
Example:
```jsx
const [value, setValue] = useState(initialValue);
```

**What does useEffect do?**
`useEffect` allows you to perform side effects in function components 
(e.g., data fetching, subscriptions, manual DOM changes). 
It runs after every render by default but can be controlled via the dependency array.
Example:
```jsx
useEffect(() => {
  document.title = `You clicked ${count} times`;
}, [count]);
```

**What is useMemo and when should you use it?**
`useMemo` caches the result of a calculation between re-renders. Use it to 
optimize performance by avoiding expensive recalculations when dependencies haven't changed.
Example:
```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

**What is useCallback and how is it different from useMemo?**
`useCallback` caches a function definition itself. While `useMemo` returns a memoized value, `useCallback` 
returns a memoized callback function. It's useful for preventing unnecessary re-renders of child components that
rely on reference equality for function props.
Example:
```jsx
const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);
```

**What is useRef used for?**
`useRef` returns a mutable ref object whose `.current` property persists across re-renders. 
It's used to access DOM elements directly or to store any mutable value that doesn't trigger a re-render when changed.
Example:
```jsx
const inputEl = useRef(null);
const onButtonClick = () => { inputEl.current.focus(); };
```

**What is the component lifecycle?**

**What is lifting state up?**
Lifting state up is a pattern where state is moved to the closest common ancestor of components that need to share or sync that state.
Example:
Moving input value state from two sibling components to their common parent so they stay in sync.

**What is prop drilling?**
Prop drilling is the process of passing data through multiple layers of components (via props)
just to get it to a deeply nested component that actually needs it.


**How does context work?**
The Context API provides a way to share values (like themes or user data) between components without having 
to explicitly pass props through every level of the tree.
Example:
```jsx
const ThemeContext = React.createContext("light");
// Use in child: const theme = useContext(ThemeContext);
```

**What is the difference between controlled and uncontrolled components?**
- Controlled: Form data is handled by a React component state.
- Uncontrolled: Form data is handled by the DOM itself (usually accessed via `useRef`).
Example:
```jsx
// Controlled
<input value={value} onChange={e => setValue(e.target.value)} />
```

**How do you optimize React performance?**
Techniques include: using `useMemo` and `useCallback`, 
lazy loading components (`React.lazy`), memoizing components (`React.memo`), 
avoiding anonymous functions in props, and optimizing list rendering with keys.

**Why are keys important in lists?**
Keys help React identify which items in a list have changed, been added, or been removed. 
They provide a stable identity for elements, allowing React to reuse existing DOM nodes instead of re-creating them, 
which improves performance and maintains component state.

Example:
```jsx
{items.map(item => <li key={item.id}>{item.text}</li>)}
```

**What causes re-renders in React?**
A component re-renders when its `state` changes, its `props` change, 
its parent component re-renders, or if it consumes a `context` that has changed.
