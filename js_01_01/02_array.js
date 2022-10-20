const numbers = [1, 2, 3, 4, 5]
// 1.
// const dobleEle = function (number) {
//   return number * 2
// }

// const newArry = numbers.map(dobleEle)

// console.log(newArry)

2.

// const newArry = numbers.map(function (number) {
//   return number * 2
// })
// console.log(newArry)
// // 3.

const newArry = numbers.map((number) => {
  return number * 2
})
console.log(newArry)