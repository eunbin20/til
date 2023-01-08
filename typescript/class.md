# What is OOP?

개발하면서 실제 세상에 존재하는 개체를 다루듯이 작업한다.

개발자 입장에서 코드를 유추하기 용이해진다.

### Class

- 자바스크립트 객체의 청사진. 여러 객체를 빠르게 복제할 수 있다.
- 객체의 형태와 포함해야 할 속성을 정의한다.
- 생성자함수의 syntactic sugar
- 클래스를 기반으로 인스턴스화되는 객체의 구성요소를 정의할 수 있다.

```jsx
class Department {
  name: stirng;

	// 생성자 메소드. 객체를 생성할 때 초기화 역할을 수행한다.
	constructor(n: string) {
	  this.name = n
  }
}

const accounting = new Department('Acounting');

console.log(accounting); // { name: 'Accounting' }

// 자바스크립트로 컴파일한 결과

var Deoartment = (function () => {
  function Department(n) {
    this.name = n;
  }
  return Department;
})();

var accounting = new Department('Accounting');
console.log(accounting);
```

### 생성자함수와 this 키워드

this는 생성된 클래스의 구체적인 인스턴스를 참조한다.

```jsx
class Department {
  name: stirng;

	// 생성자 메소드. 객체를 생성할 때 초기화 역할을 수행
	constructor(n: string) {
	  this.name = n
  }

  describe: () => {
	  cosnole.log('name: ', this.name);
  }
}

const accounting = new Department('Accounting');

const accountingCopy = { describe: accounting.describe }

accounting.describe() // "name: Accounting"
accountingCopy.describe() // "name: undefined"
```

this값은 해당 메서드가 실행될 때 결정된다.

this값이 결정되는 상황은 몇 가지가 있는데, 지금 상황과 같이 . operation으로 메서드가 실행된다면 this 값은 .앞에 오는, 즉 해당 메서드를 실행하는 인스턴스가 된다.

`accounting.describe()` 의 경우 this는 accounting이다. accounting 객체의 name 프로퍼티는 생성자 메서드에 의해 “Accounting”으로 할당되었다.

`accountingCopy.describe()` 의 경우 this는 `{ describe: accounting.describe }`

라는 더미 객체이다. 즉 name 프로퍼티를 소유하고있지 않다.

위와같은 예상치 못하게 동작하는 코드를 방지하기 위해 메소드에 매개변수를 추가해줄 수 있다.

```jsx
class Department {
  name: stirng;

	// 생성자 메소드. 객체를 생성할 때 초기화 역할을 수행
	constructor(n: string) {
	  this.name = n
  }

  // describe 메서드는 Department 인스턴스만 호출할 수 있다.
  describe: (this: Department) => {
	  cosnole.log('name: ', this.name);
  }
}

const accounting = new Department('Accounting');

accounting.describe() // "name: Accounting"

const accountingCopy = { describe: accounting.describe };

accountingCopy.describe() // 컴파일 에러

//

const accountingCopy = { name: "f", describe: accounting.describe };

accountingCopy.describe() // 해결
```

this를 통해 원치않는 동작을 바로잡을 수 잇다.

private 키워드를 통해 속성이 클래스 메서드를 통해서만 변형 가능하도록 보호.

클래스 밖에서 접근할 수 없도록 만들어줌. 오직 클래스 내부에서만(= 클래스 메소드 내부에서만) 접근할 수 있다.

클래스에서 메서드와 프로퍼티에 public, private 키워드를 붙일 수 있음.

```jsx
class Department {
  name: stirng;
	employees: string[] = [];

	// 생성자 메소드. 객체를 생성할 때 초기화 역할을 수행
	constructor(n: string) {
	  this.name = n
  }

  // describe 메서드는 Department 인스턴스만 호출할 수 있다.
  describe: (this: Department) => {
	  cosnole.log('name: ', this.name);
  }

  addEmployee(employee: string) {
	  this.employees.push(employee)
  }
}

const accounting = new Department('Accounting');

accounting.addEmploy("Anna");
accounting.addEmploy("Mery");

accounting.employees.push("Tom"); // 더 복잡한 프로젝트에서 예상치못한 결과를 야기할 수 있음.

//

class Department {
  public name: stirng; // default가 public임. 생략 가능
	private employees: string[] = []; // 클래스 외부에서 employees를 변경할 수 없음.

	// 생성자 메소드. 객체를 생성할 때 초기화 역할을 수행
	constructor(n: string) {
	  this.name = n
  }

  // describe 메서드는 Department 인스턴스만 호출할 수 있다.
  describe: (this: Department) => {
	  cosnole.log('name: ', this.name);
  }

  addEmployee(employee: string) {
	  this.employees.push(employee)
  }
}

accounting.employees.push("Tom"); // 컴파일 에러

```

자바스크립트에서는 최근까지도 private가 없음. 다 public으로 할당되어있음. 런타임도중에는 수행되지 않음.

타입스크립트에서만 유효한 키워드임.

### 간단하게 클래스 프로퍼티, 메서드 초기화하기

```jsx
class Department {
  public name: stirng;
	private id: number;

	constructor(id: number, n: string) {
		this.id = id;
	  this.name = n;
  }
}

// 위와 같이 초기화 두 번 할 필요 없음

class Department {
	// 아래와 같이 정의하면 타입스크립트에서 동일한 이름으로 속성 만들어줌.
	constructor(private id: number, public n: string) {
  }

  changeId(Id: number) {
	  this.id = id // 에러
  }
}
```

### 읽기 전용 속성(readonly)

```jsx
class Department {
	constructor(private readonly id: number, public n: string) {
  }

  changeId(Id: number) {
	  this.id = id // 에러
  }
}
```

코드의 용법을 명확하게 정의하여 예상치 못한 동작을 막을 수 있음.

### 클래스의 주요 개념

### 클래스 속성이란?

### Private, Public 한정자의 의미는?

### 클래스를 정의하는 약식 표현

### 상속

```tsx
class Department {
  protected employees: stirng[] = [];

  constructor(private readonly id: number, public n: string) {}

  addEmployee(employee: string) {
    this.employees.push(employee);
  }

  changeId(Id: number) {
    this.id = id; // 에러
  }
}

// 클래스를 상속받음
class ITDepartment extends Department {
  constructor(id: string, admins: string[]) {
    super(id, "IT");
    this.admins = admins;
  }

  // employees가 `protected`한정자로 정의되어있어 수정 가능.
  addEmployee(employee: string) {
    if (emplotyee === "Tom") return;

    this.employees.push(employee);
  }
}
```

- 상속받은 클래스에서 메소드나 프로퍼티를 수정할수도 있다.
- protected: 해당 클래스를 상속받은 클래스에서 접근 가능, 클래스 외부에서는 접근 불가능

### getter, setter

- protected로 한정되어있는 속성에 접근할 수 있음

```tsx
class Department {
  protected employees: stirng[] = [];

  get firstEmployee() {
    if (this.employees.length) {
      return this.employess[0];
    }
    throw new Error("No employee");
  }

  set firstEmployee(value: string) {
    if (!value) {
      throw new Error("no!");
    }
    this.addEmployees(value);
  }

  constructor(private readonly id: number, public n: string) {}

  addEmployee(employee: string) {
    this.employees.push(employee);
  }
}

const accounting = new Department();
// getter 메소드 실행
console.log(accounting.firstEmployee);
// setter 메소드 실행
accounting.firstEmployee = "Eunbin";
```

### 정적 속성과 정적 메서드

- 클래스의 인스턴스에서 접근할 수 없는 속성과 메서드
- 클래스에서 직접 접근 가능함
- 주로 인스턴스들을 그룹화하거나 인스턴스간의 관계, 클래스와 인스턴스간의 관계 등을 판별하기 위해 사용되는 유틸리티 함수
- 클래스에 저장하고자하는 정적 속성
- 인스턴스와는 분리되는 개념임.

ex) Math

Math.PI = 정적 속성

Math.pow(); = 정적 메서드

### 추상 클래스

abstract

상위 클래스를 상속받은 하위 클래스가 해당 메서드나 프로퍼디를 재정의할 수 있도록 기본적인 구조와 타입만 정의한다.

추상 개체를 한 개 이상 가지고있는 클래스 앞에는 abstract 키워드를 붙여야 한다.

```tsx
abstract class Department {
  protected employees: stirng[] = [];
  constructor(private readonly id: number, public n: string) {}

  abstract addEmployee(employee: string): void;
}

class ITDepartment extends Department {
  constructor(id: string, admins: string[]) {
    super(id, "IT");
    this.admins = admins;
  }

  // 상위 클래스에서 abstract로 정의되어있는 addEmployee를 재정의하지 않으면 에러가 발생한다.
  addEmployee(employee: string) {
    if (emplotyee === "Tom") return;

    this.employees.push(employee);
  }
}
```

### 싱글톤 클래스

new로 생성하지 않음.

메서드를 호출하여 구성.

특정 시점에 반드시 단 하나의 클래스 인스턴스가 존재.

### 함수 vs 클래스?

호이스팅에서 차이가 있다. 클래스는 호이스팅되지 않으므로 선언 전에 사용할 수 없다.
