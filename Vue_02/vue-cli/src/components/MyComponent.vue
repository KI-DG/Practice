<template>
  <div class="border">
    <h1>이거는 내가 만든 새로운 컴포넌트다!</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />

    <!-- <a href="url"></a> -->
    <!-- 문자열 -->
    <!-- <a v-bind:href="url"></a> -->
    <!-- js 문법임 -->
    <!-- === <a :href="url"></a> -->
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from "@/components/MyComponentItem";

export default {
  name: "MyComponent",
  // data: {
  //   url: "www.naver.com",
  // },
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: "이건 동적인 데이터!",
    };
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log("용돈없어!!");
      console.log(childData);
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다`);
    },
  },
  // vue-cli 스코프때문에 그럼
};
</script>

<style>
.border {
  border: solid 1px black;
}
</style>