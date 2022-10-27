function sleep(sec) {
  const delayUntil = Date.now() + sec
  while (Date.now() < delayUntil) {
  }
}

for (let i = 1; i <= 10; i++) {
  console.log(`${i}번째 반복`)
  sleep(1000)
}

setTimeout(function () {
  console.log("5초 뒤 실행!!")
}, 5000)