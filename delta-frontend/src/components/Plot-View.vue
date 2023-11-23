<template>
    <div class="main">
      <form @submit.prevent="handleSubmit" style="margin-top: 50px; margin-bottom: -10px;">
        <label for="symbol">Enter Stock Ticker:</label>
        <input v-model="symbol" id="symbol" type="text" required />
        <label for="startDate">Start Date:</label>
        <input v-model="startDate" id="startDate" type="date" required />
        <label for="endDate">End Date:</label>
        <input v-model="endDate" id="endDate" type="date" required />
        <button type="submit">Load Chart</button>
      </form>
      <div v-if="loading" class="spinner"></div>
      <plotly
        class="plot"
        v-if="plotData"
        :data="plotData.data"
        :layout="{
          ...plotData.layout,
          paper_bgcolor: 'rgb(77, 77, 100)',
          plot_bgcolor: 'your-desired-color',
        }"
      />
    </div>
  </template>
  
  <script>
  import { Plotly } from 'vue-plotly';
  
  export default {
    name: 'Mpld3Plot',
    components: {
      Plotly,
    },
  
    props: {
      initialSymbol: {
        type: String,
        default: 'AAPL', // Default to AAPL if no symbol is provided.
      },
    },
  
    data() {
      return {
        symbol: this.initialSymbol,
        startDate: '',
        endDate: '',
        plotData: null,
        loading: false,
      };
    },
  
    computed: {
      plotUrl() {
        return `http://localhost:5000/get-plot/${this.symbol}?start_date=${this.startDate}&end_date=${this.endDate}`;
      },
    },
  
    methods: {
      async loadPlot() {
        try {
          this.loading = true; // Show the spinner
          const response = await fetch(this.plotUrl);
          const responseData = await response.json();
          this.plotData = JSON.parse(responseData.plot);
        } catch (error) {
          console.error('Error fetching the plot:', error);
        } finally {
          this.loading = false; // Hide the spinner
        }
      },
  
      handleSubmit() {
        // Reload chart data when the form is submitted
        this.loadPlot();
      },
    },
  
    created() {
      this.loadPlot();
    },
  };
  </script>
  
  <style scoped>
  .plot {
    width: 90%;
    margin-left: auto;
    margin-right: auto;
    border: 1px;
    border-color: black;
  }
  
  form {
    margin-bottom: 20px;
  }
  
  label {
    margin-right: 10px;
  }
  
  input {
    margin-right: 10px;
  }
  
  button {
    cursor: pointer;
  }
  
  .spinner {
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-top: 4px solid #3498db;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
    display: inline-block;
    margin-left: 10px;
  }
  
  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  </style>
  