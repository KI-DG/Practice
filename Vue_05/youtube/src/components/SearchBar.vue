<template>
  <div>
    <input
      type="search"
      @keyup.enter="onInputKeyword"
      placeholder="검색어를 입력하세요"
    />
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  methods: {
    onInputKeyword(event) {
      this.$emit("input-change", event.target.value);
    },
  },
};
</script>

<style>
</style>