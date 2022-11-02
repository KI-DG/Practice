<template>
  <div>
    <h3>이것은 컴퍼넌트의 자식입니다</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput" />
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  // 선언
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null,
    };
  },
  methods: {
    childToParent: function () {
      this.$emit("child-to-parent", "나는 자식이 보낸 데이터다");
      // 객체의 기본속성값 중복 방지
    },
    childInput: function () {
      this.$emit("child-input", this.childInputData);
    },
  },
};
</script>

<style>
</style>