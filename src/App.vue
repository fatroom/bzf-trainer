<template>
  <Question :question=question></Question>
</template>

<script>
import Question from './components/Question.vue'

export default {
  name: 'App',
  components: {
    Question
  },
  data() {
    return {
      question: {
        text: "Which international organisation is of particular importance to the aeronautical radio service worldwide?",
        answers: [
          {
            id: 1,
            text: "ITU",
            correct: true
          },
          {
            id: 2,
            text: "IATA"
          },
          {
            id: 3,
            text: "UNESCO"
          },
          {
            id: 4,
            text: "NATO"
          }
        ]
      }
    }
  }
}
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
