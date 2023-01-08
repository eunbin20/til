### 인터페이스

- 객체의 구조를 설명
- 타입스크립트에만 존재하는 개념. 자바스크립트로 컴파일되지 않는다. 그래서 자바스크립트에서 제공하는 메서드와 함께 활용할 수 없음.
- 첫 글자는 대문자로 시작하는 것이 권장됨.
- initializer를 가질 수 없음

```tsx
interface Person {
  name: stirng;
  age: number;
  greet: (phrase: string) => void;
}

let user1: Person;

user1 = {
  name: "Max",
  age: 20,
  greet(phrase: string) {
    console.log(phrase + " " + this.name);
  },
};

user1.greet("Hi, I am"); // 'Hi, I am Max'
```

### 왜 필요한가?

type과 다른 점?

1. 인터페이스는 객체의 구조를 설명하기위해서만 사용됨.
   1. 무언가를 인터페이스로 정의, 그 무언가는 객체임.
2. 인터페이스를 사용하는 이유는 클래스가 인터페이스를 이행하고 준수해야하는 약속처럼 사용할 수 있기 때문.
   1. 클래스가 이 인터페이스에서 설정된 약속을 준수해야함.
   2. 쉼표를 이용해 여러 개의 인터페이스를 상속받을 수 있음.(implements)

### 왜 인터페이스인가

왜 이런 기능들을 제공할까?

클래스에서 반드시 필요한 메소드를 정의하여 안전하다.

readonly

객체가 초기화된 이후에는 변경할 수 없도록 설정.

### 함수 타입으로서의 인터페이스

```tsx
// type AddFn = (a: number, b: number) => number;
// 사용자 정의 타입의 대안으로서 interface 사용
interface AddFn {
  (a: number, b: number): number;
}

let add: AddFn;

add = (a: number, b: number) => {
  return a + b;
};
```

- 함수의 구조를 정의할 때도 사용될 수 있음

### 선택적 매개변수, 속성

?: optional operator

인터페이스는 인스턴스화할 수 없으며, 컴파일되지 않는다. 클래스는 인스턴스화할 수 있으며 컴파일된다.

인터페이스는 순수 타입스크립트의 기능

클래스나 객체가 특정 구조를 갖추도록 하고 객체의 형태에 대한 개념을 명확하게 설명하는 강력한 기능.

필요에 따라 타입으로 대체할 수 있음.

인터페이스를 사용하는 것이 일반적.

타입스크립트 초기에는 type으로는 인터페이스처럼 구현하거나 사용할 수 없었다. 유연성이 전보다 향상되긴 했지만 객체를 사용하여 작업을 수행하고 구조를 설명하고자한다면 인터페이스를 사용하는 것이 권장된다.

[Documentation - Object Types](https://www.typescriptlang.org/docs/handbook/2/objects.html)

[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
