# React Questions

**What is React and how does it work?**

React is a JavaScript library for building user interfaces.
It works by creating a virtual representation of the UI (Virtual DOM) and efficiently
updating the actual DOM only where changes have occurred using a process called reconciliation.

---

**What is the virtual DOM?**

The Virtual DOM is a lightweight copy of the actual DOM kept in memory.
React uses it to calculate the minimal number of changes needed to update the UI,
improving performance by avoiding expensive direct DOM manipulations.

When a component's state changes, React creates a new Virtual DOM tree and compares it with the previous one (diffing).

---

**What is the difference between props and state?**

- `props`: Short for properties, passed from parent to child components. They are read-only (immutable) from the child's perspective.
- `state`: Managed within the component itself. It is mutable (via setter functions) and triggers a re-render when it changes.

```jsx
function Welcome(props) {
  const [count, setCount] = useState(0); // State
  return <h1>Hello, {props.name}</h1>;   // Props
}
```

---

**What are hooks?**

Hooks are functions that let you "hook into" React state and lifecycle features from function components.
Examples include `useState`, `useEffect`, and `useContext`.

```jsx
const [value, setValue] = useState(initialValue);
```

---

**What does useEffect do?**

`useEffect` allows you to perform side effects in function components
(e.g., data fetching, subscriptions, manual DOM changes).
It runs after every render by default but can be controlled via the dependency array.

```jsx
useEffect(() => {
  document.title = `You clicked ${count} times`;
}, [count]);
```

---

**What is useMemo and when should you use it?**

`useMemo` caches the result of a calculation between re-renders. Use it to
optimize performance by avoiding expensive recalculations when dependencies haven't changed.

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

---

**What is useCallback and how is it different from useMemo?**

`useCallback` caches a function definition itself. While `useMemo` returns a memoized value, `useCallback`
returns a memoized callback function. It's useful for preventing unnecessary re-renders of child components that
rely on reference equality for function props.

```jsx
const memoizedCallback = useCallback(() => { doSomething(a, b); }, [a, b]);
```

---

**What is useRef used for?**

`useRef` returns a mutable ref object whose `.current` property persists across re-renders.
It's used to access DOM elements directly or to store any mutable value that doesn't trigger a re-render when changed.

```jsx
const inputEl = useRef(null);
const onButtonClick = () => { inputEl.current.focus(); };
```

---

**What is lifting state up?**

Lifting state up is a pattern where state is moved to the closest common ancestor of components that need to share or sync that state.

Moving input value state from two sibling components to their common parent so they stay in sync.

---

**What is prop drilling?**

Prop drilling is the process of passing data through multiple layers of components (via props)
just to get it to a deeply nested component that actually needs it.

---

**How does context work?**

The Context API provides a way to share values (like themes or user data) between components without having
to explicitly pass props through every level of the tree.

```jsx
const ThemeContext = React.createContext("light");
// Use in child: const theme = useContext(ThemeContext);
```

---

**What is the difference between controlled and uncontrolled components?**

- Controlled: Form data is handled by a React component state.
- Uncontrolled: Form data is handled by the DOM itself (usually accessed via `useRef`).

```jsx
// Controlled
<input value={value} onChange={e => setValue(e.target.value)} />
```

---

**How do you optimize React performance?**

Techniques include: using `useMemo` and `useCallback`,
lazy loading components (`React.lazy`), memoizing components (`React.memo`),
avoiding anonymous functions in props, and optimizing list rendering with keys.

---

**Why are keys important in lists?**

Keys help React identify which items in a list have changed, been added, or been removed.
They provide a stable identity for elements, allowing React to reuse existing DOM nodes instead of re-creating them,
which improves performance and maintains component state.

```jsx
{items.map(item => <li key={item.id}>{item.text}</li>)}
```

---

**What causes re-renders in React?**

A component re-renders when its `state` changes, its `props` change,
its parent component re-renders, or if it consumes a `context` that has changed.

---

**What is the component lifecycle?**

Function components don't have lifecycle methods, but `useEffect` covers the same phases:

| Class lifecycle | Function component equivalent |
|---|---|
| `componentDidMount` | `useEffect(() => { ... }, [])` — runs once after first render |
| `componentDidUpdate` | `useEffect(() => { ... }, [dep])` — runs when dep changes |
| `componentWillUnmount` | Return a cleanup function from `useEffect` |

```jsx
useEffect(() => {
  const sub = subscribe(id);        // mount / update
  return () => sub.unsubscribe();   // unmount / before next effect
}, [id]);
```

React's render cycle: **render → commit → effects**. The render phase is pure (no side effects); the commit phase applies DOM changes; effects run after commit.

---

**What is useReducer and when should you use it?**

`useReducer` is an alternative to `useState` for complex state logic. It takes a reducer function `(state, action) => newState` and an initial state, and returns the current state plus a `dispatch` function — the same pattern as Redux.

Use it when:
- Next state depends on the previous state in non-trivial ways
- Multiple sub-values update together
- State transitions are easier to reason about as explicit action types

```jsx
const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case "increment": return { count: state.count + 1 };
    case "decrement": return { count: state.count - 1 };
    case "reset":     return initialState;
    default:          throw new Error("Unknown action");
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      <p>{state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
    </>
  );
}
```

---

**What are custom hooks?**

A custom hook is a regular JavaScript function whose name starts with `use` and that calls other hooks. They let you extract and share stateful logic between components without changing component hierarchy.

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);

  return { data, loading, error };
}
```

---

**What is React.memo?**

`React.memo` is a higher-order component that memoizes a component's output. If the parent re-renders but the child's props haven't changed (shallow comparison), React skips re-rendering the child.

```jsx
const ExpensiveList = React.memo(function ExpensiveList({ items }) {
  return <ul>{items.map(i => <li key={i.id}>{i.name}</li>)}</ul>;
});
```

Pair it with `useCallback` for function props — otherwise a new function reference on every parent render will bust the memo:

```jsx
const handleClick = useCallback(() => doSomething(id), [id]);
<ExpensiveList items={items} onClick={handleClick} />
```

---

**What are error boundaries?**

Error boundaries are class components that catch JavaScript errors anywhere in their child tree during rendering, in lifecycle methods, or in constructors, and display a fallback UI instead of crashing the whole app.

```jsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    logError(error, info.componentStack);
  }

  render() {
    if (this.state.hasError) return <h2>Something went wrong.</h2>;
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <MyWidget />
</ErrorBoundary>
```

Error boundaries do *not* catch errors in event handlers (use try/catch there) or in async code.

---

**What is React.lazy and Suspense?**

`React.lazy` lets you code-split a component so its bundle is loaded only when it is first rendered. `Suspense` provides a fallback UI while the lazy component's module is loading.

```jsx
const Settings = React.lazy(() => import("./Settings"));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Settings />
    </Suspense>
  );
}
```

This is the primary built-in mechanism for route-level code splitting.

---

**What is automatic batching in React 18?**

Before React 18, state updates inside `setTimeout`, Promises, or native event handlers were *not* batched — each update caused a separate re-render. React 18 automatically batches all updates everywhere.

```jsx
// React 18: both setA and setB are batched → 1 re-render
setTimeout(() => {
  setA(1);
  setB(2);
}, 0);

// Opt out if needed
import { flushSync } from "react-dom";
flushSync(() => setA(1)); // forces immediate render
```

---

**What is useTransition?**

`useTransition` marks a state update as non-urgent (a "transition"), allowing React to keep the UI responsive while the transition is in progress. React can interrupt a transition to handle urgent updates (like typing).

```jsx
const [isPending, startTransition] = useTransition();

function handleFilter(query) {
  startTransition(() => {
    setFilteredList(expensiveFilter(query)); // non-urgent
  });
}

return isPending ? <Spinner /> : <List items={filteredList} />;
```

`useDeferredValue` is the prop-level equivalent — it defers re-rendering a part of the tree that depends on a fast-changing value.

---

**What are React portals?**

Portals let you render a component into a different DOM node than its parent, while keeping it in the same React component tree (so events still bubble through React's tree).

```jsx
import { createPortal } from "react-dom";

function Modal({ children }) {
  return createPortal(
    <div className="modal">{children}</div>,
    document.getElementById("modal-root") // render outside #app
  );
}
```

Useful for modals, tooltips, and dropdowns that need to escape `overflow: hidden` or z-index stacking contexts.

---

**What is forwardRef?**

`forwardRef` lets a parent pass a `ref` through a component to a DOM element (or another component) inside it. Without it, refs don't pass through function components.

```jsx
const FancyInput = React.forwardRef((props, ref) => (
  <input ref={ref} {...props} className="fancy" />
));

function Form() {
  const inputRef = useRef(null);
  return (
    <>
      <FancyInput ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>Focus</button>
    </>
  );
}
```
