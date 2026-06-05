# TypeScript Questions

**What is the difference between type and interface?**

- `interface`: Primarily for defining object shapes.
  Supports declaration merging (you can define the same interface multiple times and they will merge).
- `type`: Can define objects but also primitives, unions, tuples, and intersections.
  Does not support declaration merging.

```typescript
interface User { name: string; }
type ID = number | string;
```

---

**What are union and intersection types?**

- Union (`|`): Allows a value to be one of several types (e.g., `string | number`).
- Intersection (`&`): Combines multiple types into one, requiring the value to satisfy all combined types.

```typescript
type Status = "success" | "error";
type AdminUser = User & { role: string };
```

---

**What is type narrowing?**

Type narrowing is the process of refining a type from a broader type to a more specific
type using conditional checks (e.g., `typeof`, `instanceof`, or truthiness checks).

```typescript
function print(val: string | number) {
  if (typeof val === "string") {
    console.log(val.toUpperCase()); // Narrowed to string
  }
}
```

---

**What is a type guard?**

A type guard is an expression that performs a runtime check to guarantee the type in some scope.
It can be a simple `typeof` check or a custom function using the `is` keyword (Type Predicate).

```typescript
function isString(val: any): val is string {
  return typeof val === "string";
}
```

---

**What is unknown vs any?**

- `any`: Opts out of type checking entirely. You can do anything with an `any` type.
- `unknown`: The type-safe counterpart of `any`. You can assign anything to `unknown`,
  but you cannot perform operations on it without first narrowing the type.

```typescript
let val: unknown = "Hello";
// val.toUpperCase(); // Error
if (typeof val === "string") val.toUpperCase(); // OK
```

---

**What is structural typing?**

TypeScript uses a structural type system (also called duck typing).
If two types have the same shape (the same members), they are considered compatible, regardless of their explicit declarations.

```typescript
interface Point { x: number; y: number; }
const p: Point = { x: 10, y: 20, z: 30 }; // OK, has required members
```

---

**What is an enum, and should you use it?**

Enums allow defining a set of named constants. While they provide clarity, they can have pitfalls
(like numeric enums being not fully type-safe or increasing bundle size).
Many developers prefer `const object` or union types of string literals instead.

```typescript
enum Color { Red, Green, Blue }
let c: Color = Color.Green;
```

---

**What are optional and readonly properties?**

- Optional (`?`): Properties that may or may not be present on an object.
- `readonly`: Properties that cannot be modified after the object is initialized.

```typescript
interface Car {
  readonly brand: string;
  model?: string;
}
```

---

**What is never used for?**

The `never` type represents the type of values that never occur.
It's used for functions that always throw an error, infinite loops, or to handle "impossible" cases in exhaustive type checking.

```typescript
function throwError(msg: string): never {
  throw new Error(msg);
}
```

---

**What's the difference between compile-time and runtime types?**

Compile-time types exist only during TypeScript compilation for type checking and are removed (erased)
during the transpilation to JavaScript. Runtime types are the actual types of values as they exist
when the code is executed in the browser or Node.js.

```typescript
// TS: let x: number = 5;
// JS: let x = 5; (type information is gone)
```

---

**What are generics?**

Generics let you write reusable code that works over a variety of types while preserving type safety. Instead of using `any`, you use a type parameter (commonly `T`) that is filled in at the call site.

```typescript
function identity<T>(value: T): T {
  return value;
}

identity<string>("hello"); // type: string
identity<number>(42);      // type: number
identity("inferred");      // TS infers T = string

// Generic constraint
function getLength<T extends { length: number }>(val: T): number {
  return val.length;
}
getLength("abc"); // 3
getLength([1, 2]); // 2
```

Generics are everywhere: `Array<T>`, `Promise<T>`, `Map<K, V>`.

---

**What are the most useful built-in utility types?**

TypeScript ships with utility types that transform existing types:

| Utility | What it does |
|---|---|
| `Partial<T>` | All properties of T become optional |
| `Required<T>` | All properties of T become required |
| `Readonly<T>` | All properties become readonly |
| `Pick<T, K>` | Keep only keys K from T |
| `Omit<T, K>` | Remove keys K from T |
| `Record<K, V>` | Object type with keys K and values V |
| `ReturnType<F>` | Extract the return type of a function |
| `Parameters<F>` | Extract parameter types of a function as a tuple |
| `NonNullable<T>` | Remove null and undefined from T |
| `Awaited<T>` | Unwrap a Promise type |

```typescript
interface User { id: number; name: string; email: string; }

type NewUser    = Omit<User, "id">;           // { name, email }
type Preview    = Pick<User, "id" | "name">; // { id, name }
type PatchUser  = Partial<User>;             // all fields optional
type PageMap    = Record<string, User[]>;    // { [key: string]: User[] }

async function fetchUser(): Promise<User> { /* ... */ return {} as User; }
type FetchReturn = Awaited<ReturnType<typeof fetchUser>>; // User
```

---

**What are mapped types?**

Mapped types create new types by iterating over the keys of an existing type with `in keyof`.

```typescript
// Reimplementing Partial manually
type MyPartial<T> = {
  [K in keyof T]?: T[K];
};

// Make all values nullable
type Nullable<T> = {
  [K in keyof T]: T[K] | null;
};

// Prefix every key with "get_"
type Getters<T> = {
  [K in keyof T as `get_${string & K}`]: () => T[K];
};
```

---

**What are conditional types?**

Conditional types select a type based on a condition using `extends`:

```typescript
type IsString<T> = T extends string ? "yes" : "no";

type A = IsString<string>;  // "yes"
type B = IsString<number>;  // "no"

// Practical use: unwrap arrays
type Flatten<T> = T extends Array<infer U> ? U : T;
type Num = Flatten<number[]>; // number
type Str = Flatten<string>;   // string
```

`infer` lets you capture a sub-type from within the condition.

---

**What is as const and what does satisfies do?**

- `as const`: narrows a value to its literal type and makes all properties `readonly`. Useful when you want TypeScript to treat an object's values as exact string/number literals rather than widened types.

```typescript
const colors = ["red", "green", "blue"] as const;
// type: readonly ["red", "green", "blue"]
// Without as const → string[]

type Color = typeof colors[number]; // "red" | "green" | "blue"
```

- `satisfies` (TS 4.9+): validates that a value matches a type *without widening* the inferred type. You get both the constraint check and the precise inferred type.

```typescript
type Palette = Record<string, string>;

const palette = {
  red: "#ff0000",
  green: "#00ff00",
} satisfies Palette;

palette.red.toUpperCase(); // OK — still typed as string literal, not just string
```

---

**What are template literal types?**

Template literal types compose string literal types using template syntax, enabling precise string-based APIs.

```typescript
type EventName = "click" | "focus" | "blur";
type Handler = `on${Capitalize<EventName>}`; // "onClick" | "onFocus" | "onBlur"

type CSSUnit = "px" | "rem" | "em";
type CSSValue = `${number}${CSSUnit}`; // "10px", "1.5rem", etc. (structurally)
```

---

**What is the difference between strict mode flags?**

`strict: true` in `tsconfig.json` enables a family of checks:

- `strictNullChecks` — `null` and `undefined` are not assignable to other types without explicit handling. The most impactful flag.
- `noImplicitAny` — error when a variable's type is inferred as `any`.
- `strictFunctionTypes` — stricter checking of function parameter types (contravariance).
- `noUncheckedIndexedAccess` — array/object index access returns `T | undefined` instead of just `T`.

Always enable `strict: true` in new projects.

---

**What are declaration files (.d.ts)?**

Declaration files describe the shape of existing JavaScript to TypeScript without containing runnable code. They are used to type third-party libraries that weren't written in TypeScript.

```typescript
// math.d.ts
export declare function add(a: number, b: number): number;
export declare const PI: number;
```

Packages in `@types/*` (e.g., `@types/lodash`) are community-maintained declaration files for popular JS libraries. When a library ships its own types, `@types` is not needed.
