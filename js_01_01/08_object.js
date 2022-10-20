const myInfo = {
  name: 'jack',
  phoneNumber: '123456',
  'samsung product': {
    buds: 'Buds pro',
    galaxy: 'S99',
  },
}

console.log(myInfo.name)
console.log(myInfo['name'])
console.log(myInfo['samsung product'])
console.log(myInfo['samsung product'].galaxy)

const obj = {
  name: 'jack',
  greeting() {
    console.log('hi!')
  }
}

console.log(obj.name)
console.log(obj.greeting())





const jsonData = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}

const objTojson = JSON.stringify(jsonData)

console.log(objTojson)
console.log(typeof objTojson)

const jsonTobj = JSON.parse(objTojson)

console.log(jsonTobj)
console.log(typeof jsonTobj)
