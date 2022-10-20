const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)
console.log(numbers[numbers.length - 1])

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))
console.log(numbers.indexOf(100))

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('_'))


const colors = ['red', 'blue', 'green']
// 1.
// const printClr = function (color) {
//   console.log(color)
// }
// colors.forEach(printClr)
// 2.
// colors.forEach(function (color) {
//   console.log(color)
// })

colors.forEach((color) => {
  console.log(color)
})
