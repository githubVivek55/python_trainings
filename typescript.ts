type A = {
  name: string;
};

type B = {
  age: number;
};

type C = A &
  B & {
    address: string;
  };

const person: C = {
  name: 'John Doe',
  age: 30,
  address: '123 Main St',
};
