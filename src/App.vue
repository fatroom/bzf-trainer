<template>
  <Question :question=nextQuestion @next-question="selectNextQuestion()"></Question>
</template>

<script>
import Question from './components/Question.vue'
import {ref} from 'vue'

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

let questions = [
  {
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
  },
  {
    text: "What is the legal basis for the setting-up and operation of radio installations in the Federal Republic of Germany?",
    answers: [
      {
        id: 1,
        text: "Telecommunications Act (TKG)",
        correct: true,
      },
      {
        text: "Air Traffic Act (LuftVG)",
        id: 2,
      },
      {
        text: "Convention on International Civil Aviation",
        id: 3,
      },
      {
        text: "Ordinance on the fitting of aircraft with navigational equipment",
        id: 4,
      }
    ]
  }
]


export default {
  name: 'App',
  components: {
    Question
  },

  setup() {
    const questionIdx = ref(Math.floor(Math.random() * questions.length));
    return {
      questionIdx
    }
  },
  computed: {
    nextQuestion() {
      return questions[this.questionIdx]
    }
  },
  methods: {
    selectNextQuestion() {
      this.questionIdx = Math.floor(Math.random() * questions.length);
      let question = questions[this.questionIdx]
      shuffleArray(question.answers)
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
