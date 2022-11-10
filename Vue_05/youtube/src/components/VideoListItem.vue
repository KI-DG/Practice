<template>
  <li @click="selectVideoItem" style="display: flex">
    <img :src="video.snippet.thumbnails.default.url" alt="video-thumbnamil" />
    <span>{{ video.snippet.title }}</span>
    <br />
  </li>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: Object,
  },
  methods: {
    selectVideoItem() {
      this.$emit("select-video-item", this.video);
    },
  },
};
</script>

<style>
</style>