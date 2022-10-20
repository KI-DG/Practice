const arr = [1, 2, 3, 4, 5]

// const result = arr.every(function (elem) {
//   return elem % 2 === 0
// })

// console.log(result)

// const result = arr.every((elem) => {
//   return elem % 2 === 0
// })
// console.log(result)

const result = arr.every((elem) => elem % 2 === 0)
console.log(result)
