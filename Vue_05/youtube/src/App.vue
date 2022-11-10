<template>
  <div id="app">
    <SearchBar @input-change="onInputChange" />
    <MainVideo :video="mainVideo" />
    <VideoList
      :videos="videos.slice(1)"
      @select-video-item="onMainVideoChange"
    />
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar";
import MainVideo from "@/components/MainVideo";
import VideoList from "@/components/VideoList";
import axios from "axios";

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
const API_URL = "https://www.googleapis.com/youtube/v3/search";

export default {
  name: "App",
  components: {
    SearchBar,
    MainVideo,
    VideoList,
  },
  data() {
    return {
      inputValue: null,
      videos: [],
      mainVideo: null,
    };
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText;

      axios({
        method: "get",
        url: API_URL,
        params: {
          key: API_KEY,
          part: "snippet",
          type: "video",
          q: this.inputValue,
        },
      })
        .then((response) => {
          console.log(response);
          this.videos = response.data.items;
          this.mainVideo = this.videos[0];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    onMainVideoChange(video) {
      this.mainVideo = video;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
