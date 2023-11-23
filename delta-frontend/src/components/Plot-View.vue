<template>
    <div>
        <plotly :data="plotData.data" :layout="plotData.layout"/>
    </div>
</template>


<script>
import { Plotly } from 'vue-plotly'

export default {
    name: 'Mpld3Plot',
    components: {
        Plotly
    },

    props: {
        symbol: {
            type: String,
            default: "AAPL"  // Default to AAPL if no symbol is provided.
        }
    },

    computed: {
        plotUrl() {
            return `http://localhost:5000/get-plot/${this.symbol}`;
        }
    },

    methods: {
        async loadPlot() {
            try {
                const response = await fetch(this.plotUrl);
                const responseData = await response.json();
                this.plotData = JSON.parse(responseData.plot);
            } catch (error) {
                console.error("Error fetching the plot:", error);
            }
        }
    },

    created() {
        this.loadPlot();
    },

    data() {
    return {
        plotData: ""
    };
}

}
</script>

<style scoped>

</style>

