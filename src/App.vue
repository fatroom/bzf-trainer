<template>
  <Question :question=question @next-question="selectNextQuestion()"></Question>
</template>

<script>
import Question from './components/Question.vue'
import {ref} from 'vue'
import questions from '../public/data/bzf.json'

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

export default {
  name: 'App',
  components: {
    Question
  },

  setup() {
    const questionIdx = Math.floor(Math.random() * questions.length);
    const question = ref(questions[questionIdx])
    return {
      question
    }
  },

  methods: {
    selectNextQuestion() {
      let questionIdx = Math.floor(Math.random() * questions.length);
      this.question = questions[questionIdx]
      shuffleArray(this.question.answers);
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
