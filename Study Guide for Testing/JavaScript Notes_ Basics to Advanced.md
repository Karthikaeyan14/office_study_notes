# JavaScript Notes: Basics to Advanced

## 1. Basics

JavaScript (JS) is a high-level, interpreted, single-threaded language that runs in browsers and on servers (Node.js).

```js
console.log("Hello, World!");   // output
// single-line comment
/* multi-line comment */
```

---

## 2. Variables: `var` vs `let` vs `const`

```js
var a = 1;      // function-scoped, old
let b = 2;      // block-scoped, reassignable
const c = 3;    // block-scoped, NOT reassignable
```

| Feature | `var` | `let` | `const` |
| --- | --- | --- | --- |
| Scope | Function | Block `{}` | Block `{}` |
| Re-declare in same scope | Allowed | Error | Error |
| Re-assign | Yes | Yes | No |
| Hoisting | Hoisted, initialised as `undefined` | Hoisted, but in Temporal Dead Zone (error if used early) | Same as `let` |
| Must initialise at declaration | No | No | Yes |
| Global object property (`window.x`) | Yes | No | No |

```js
// Scope difference
if (true) {
  var x = 10;
  let y = 20;
}
console.log(x); // 10  (var leaks out of block)
console.log(y); // ReferenceError

// Hoisting difference
console.log(p); // undefined
var p = 5;
console.log(q); // ReferenceError (TDZ)
let q = 5;

// const with objects: the reference is fixed, content can change
const user = { name: "Ravi" };
user.name = "Arun";   // OK
user = {};            // TypeError
```

**Loop gotcha (closures):**

```js
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i)); // 3 3 3
for (let j = 0; j < 3; j++) setTimeout(() => console.log(j)); // 0 1 2
```

**Best practice:** use `const` by default, `let` when reassignment is needed, avoid `var`.

---

## 3. Data Types

### Primitive (stored by value, immutable)

| Type | Example |
| --- | --- |
| Number | `42`, `3.14`, `NaN`, `Infinity` |
| String | `"hi"`, `'hi'`, `` `hi` `` |
| Boolean | `true`, `false` |
| Undefined | `let a;` (declared, no value) |
| Null | `let a = null;` (intentional empty) |
| Symbol | `Symbol("id")` (unique identifier) |
| BigInt | `123n` (very large integers) |

### Non-primitive / Reference (stored by reference)

Object, Array, Function, Date, Map, Set, etc.

```js
typeof 42;          // "number"
typeof "a";         // "string"
typeof undefined;   // "undefined"
typeof null;        // "object"  (a historic bug)
typeof [];          // "object"
typeof function(){};// "function"
Array.isArray([]);  // true
```

### Primitive vs Reference

```js
let a = 5; let b = a; b = 10;
console.log(a); // 5 (copy)

let o1 = { n: 1 }; let o2 = o1; o2.n = 99;
console.log(o1.n); // 99 (same object)
```

### `null` vs `undefined`

| `undefined` | `null` |
| --- | --- |
| Variable declared but not assigned | Value intentionally set to "nothing" |
| Type: `undefined` | Type: `object` |
| Set by JS | Set by the programmer |
| `null == undefined` → true | `null === undefined` → false |

### Type conversion

```js
Number("5");      // 5
String(5);        // "5"
Boolean("");      // false
"5" + 1;          // "51" (coercion to string)
"5" - 1;          // 4   (coercion to number)
```

Falsy values: `false, 0, "", null, undefined, NaN, 0n`. Everything else is truthy.

---

## 4. Operators

```js
// Arithmetic: + - * / % **
// Assignment: = += -= *= /=
// Comparison: == != === !== > < >= <=
// Logical: && || !
// Ternary
let msg = age >= 18 ? "Adult" : "Minor";
// Nullish coalescing & optional chaining
let n = value ?? "default";     // only for null/undefined
let city = user?.address?.city; // no error if address is missing
```

### `==` vs `===`

```js
5 == "5";    // true  (type coercion)
5 === "5";   // false (strict: value AND type)
```

Always prefer `===`.

---

## 5. Control Flow

```js
if (x > 0) { } else if (x === 0) { } else { }

switch (day) {
  case 1: console.log("Mon"); break;
  default: console.log("Other");
}

for (let i = 0; i < 5; i++) { }
while (cond) { }
do { } while (cond);

for (const item of [1, 2, 3]) { }        // values of iterables
for (const key in { a: 1, b: 2 }) { }    // keys of an object
```

| `for...of` | `for...in` |
| --- | --- |
| Iterates **values** (arrays, strings, Map, Set) | Iterates **keys/indexes** (objects) |
| Not for plain objects | Avoid for arrays |

`break` exits the loop; `continue` skips to the next iteration.

---

## 6. Functions

```js
// Declaration (hoisted)
function add(a, b) { return a + b; }

// Expression (not hoisted)
const sub = function (a, b) { return a - b; };

// Arrow function
const mul = (a, b) => a * b;

// Default, rest, spread
function greet(name = "Guest") { return `Hi ${name}`; }
function sum(...nums) { return nums.reduce((a, b) => a + b, 0); }
Math.max(...[1, 5, 3]);   // 5

// IIFE (runs immediately)
(function () { console.log("run"); })();
```

### Declaration vs Expression vs Arrow

|  | Declaration | Expression | Arrow |
| --- | --- | --- | --- |
| Hoisted | Yes (fully) | No | No |
| Own `this` | Yes | Yes | No (inherits) |
| Own `arguments` | Yes | Yes | No |
| Usable as constructor (`new`) | Yes | Yes | No |

### Higher-order & callback

```js
function run(fn) { fn(); }
run(() => console.log("callback"));
```

---

## 7. Strings, Arrays, Objects

### Strings

```js
const s = "JavaScript";
s.length; s.toUpperCase(); s.slice(0, 4); s.includes("Script");
s.split(""); s.replace("Java", "Type"); s.trim();
`Template: ${1 + 2}`;   // template literal
```

### Arrays

```js
const arr = [1, 2, 3];
arr.push(4);  arr.pop();  arr.shift();  arr.unshift(0);

arr.map(x => x * 2);            // new array
arr.filter(x => x > 1);         // new array
arr.reduce((acc, x) => acc + x, 0);
arr.find(x => x > 1);  arr.some(...);  arr.every(...);
arr.includes(2);  arr.indexOf(2);  arr.sort((a, b) => a - b);
[...arr, 5];  const [first, second] = arr;   // spread, destructuring
```

| `map` | `forEach` |
| --- | --- |
| Returns a new array | Returns `undefined` |
| Chainable | Not chainable |

| `slice` | `splice` |
| --- | --- |
| Returns a copy of a part | Adds/removes elements |
| Does **not** change original | **Changes** original |

### Objects

```js
const person = {
  name: "Asha",
  age: 22,
  greet() { return `Hi, ${this.name}`; }
};
person.name; person["age"]; person.city = "Chennai"; delete person.age;
Object.keys(person); Object.values(person); Object.entries(person);
const { name, age = 18 } = person;          // destructuring
const copy = { ...person, role: "dev" };    // spread
```

**Shallow vs deep copy**

```js
const shallow = { ...obj };               // nested objects still shared
const deep = structuredClone(obj);        // fully independent
```

### Map & Set

```js
const set = new Set([1, 2, 2, 3]);   // unique values: {1,2,3}
const map = new Map(); map.set("a", 1); map.get("a");
```

Map allows any type as key; plain objects only strings/symbols.

---

## 8. Scope, Hoisting, Closures

**Scope:** global, function, block. Inner scopes can read outer variables (scope chain).

**Hoisting:** declarations are moved to the top of their scope during compilation.

**Closure:** a function that remembers variables from where it was created.

```js
function counter() {
  let count = 0;
  return () => ++count;
}
const c = counter();
c(); // 1
c(); // 2
```

Use cases: data privacy, function factories, callbacks.

---

## 9. `this` keyword

```js
console.log(this);            // global/window (or undefined in modules)
obj.method();                 // this = obj
new Person();                 // this = new object
const f = () => this;         // arrow: this from surrounding scope
```

### `call`, `apply`, `bind`

```js
function hi(g) { return `${g} ${this.name}`; }
hi.call({ name: "A" }, "Hello");      // args one by one, runs now
hi.apply({ name: "A" }, ["Hello"]);   // args as array, runs now
const b = hi.bind({ name: "A" });     // returns new function
b("Hello");
```

---

## 10. Objects, Prototypes, Classes (OOP)

```js
// Constructor function
function Person(name) { this.name = name; }
Person.prototype.say = function () { return this.name; };

// ES6 class
class Animal {
  #secret = 1;                       // private field
  static count = 0;                  // static
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound`; }
  get info() { return this.name; }   // getter
}
class Dog extends Animal {
  speak() { return `${super.speak()} - Woof`; }
}
new Dog("Tommy").speak();
```

**Prototype chain:** if a property isn't found on an object, JS looks up its `__proto__` chain until `null`.

Four pillars: Encapsulation, Inheritance, Polymorphism, Abstraction.

---

## 11. ES6+ Features (Modern JS)

- `let`, `const`, arrow functions, template literals
- Destructuring, spread/rest, default parameters
- Classes, modules, `Map`/`Set`, `Symbol`
- Optional chaining `?.`, nullish `??`
- `Promise`, `async/await`
- `Array.flat()`, `Object.fromEntries()`, `structuredClone()`

---

## 12. Error Handling

```js
try {
  JSON.parse("{bad json}");
} catch (err) {
  console.error(err.message);
} finally {
  console.log("always runs");
}
throw new Error("Custom error");
```

---

## 13. Asynchronous JavaScript

JS is single-threaded; async work is handled by the **event loop**.

Order: call stack → microtask queue (Promises) → macrotask queue (`setTimeout`, events).

```js
console.log(1);
setTimeout(() => console.log(2), 0);
Promise.resolve().then(() => console.log(3));
console.log(4);
// Output: 1 4 3 2
```

### Callback → Promise → async/await

```js
// Callback (leads to "callback hell")
getData(function (res) { process(res, function () { /* ... */ }); });

// Promise
fetch(url)
  .then(r => r.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// async/await (cleanest)
async function load() {
  try {
    const res = await fetch(url);
    const data = await res.json();
    return data;
  } catch (e) { console.error(e); }
}

// Parallel
await Promise.all([p1, p2]);        // all succeed or fail fast
await Promise.allSettled([p1, p2]); // wait for all, never rejects
await Promise.race([p1, p2]);       // first to settle
```

---

## 14. Modules

```js
// math.js
export const PI = 3.14;
export default function add(a, b) { return a + b; }

// app.js
import add, { PI } from "./math.js";
```

---

## 15. DOM & Events (Browser)

```js
const btn = document.querySelector("#btn");
btn.addEventListener("click", (e) => {
  e.preventDefault();
  btn.textContent = "Clicked";
});
document.createElement("div");
parent.appendChild(child);
element.classList.toggle("active");
```

**Event bubbling** goes child → parent; **capturing** goes parent → child. **Event delegation** means attaching one listener to a parent to handle many children.

---

## 16. Advanced Concepts

- **Currying:** `const add = a => b => a + b; add(2)(3);`
- **Debounce / Throttle:** limit how often a function runs (search boxes, scroll).
- **Generators:** `function* g(){ yield 1; yield 2; }`
- **Iterators & Symbol.iterator**
- **Proxy & Reflect:** intercept object operations.
- **WeakMap / WeakSet:** hold weak references, helps garbage collection.
- **Memoization:** cache function results.
- **Web Storage:** `localStorage`, `sessionStorage`, cookies.
- **Memory management:** automatic garbage collection (mark and sweep).

```js
function debounce(fn, delay) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), delay);
  };
}
```

---

## 17. More Key Differences (Quick Reference)

| Topic | Difference |
| --- | --- |
| `var` vs `let` vs `const` | See section 2 |
| `==` vs `===` | Loose (coerces) vs strict (type + value) |
| `null` vs `undefined` | Intentional empty vs not assigned |
| Primitive vs Reference | Copied by value vs shared by reference |
| `map` vs `forEach` | Returns new array vs returns nothing |
| `slice` vs `splice` | Non-mutating copy vs mutating add/remove |
| `for...in` vs `for...of` | Keys vs values |
| `call` vs `apply` vs `bind` | Args list, args array, returns new function |
| Function declaration vs expression | Hoisted vs not hoisted |
| Arrow vs regular function | No own `this`/`arguments`/`new` |
| `localStorage` vs `sessionStorage` | Persists until cleared vs cleared on tab close |
| Shallow vs deep copy | Nested objects shared vs fully independent |
| Synchronous vs asynchronous | Blocks execution vs non-blocking via event loop |
| `Object.freeze` vs `const` | Freeze makes object immutable; `const` only blocks reassignment |
| Promise vs async/await | Chained `.then` vs synchronous-looking syntax over Promises |

---

## 18. Learning Roadmap

1. Syntax, variables, data types, operators
2. Conditions, loops, functions
3. Arrays, objects, string methods
4. Scope, hoisting, closures, `this`
5. DOM and events
6. ES6+ features, classes, modules
7. Async JS (Promises, async/await, fetch)
8. Advanced patterns, then a framework (React, Node.js)

Practice by building small projects: to-do list, calculator, weather app, quiz app.
