function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))

const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(2, 7))

const greeting = function (name = 'Anonmous') {
  return `Hi ${name}`
}
// 1단계
// const greeting = (name) => {
//   return `Hi ${name}`
// }
// 2단계 - 에어비앤비에서 권장하지 않음
// const greeting = name =>{
//   return `Hi ${name}`
// }
// 3단계 - (name) 에어비앤비에서는 이렇게 권장 name 으로 써도 됨
// const greeting = (name) => `HI ${name}`


console.log(greeting())

const noArgs = function () {
  return 0
}

console.log(noArgs(1, 2, 3))

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}

console.log(twoArgs(1, 2, 3))

const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

console.log(threeArgs())
console.log(threeArgs(1))
console.log(threeArgs(1, 2))


  // function (num) {
  //   return num ** 3
  // }

  // (num) => { return num ** 3 }

  // ((num) => num ** 3)(2)

