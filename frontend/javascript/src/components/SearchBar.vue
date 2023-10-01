<template>
    <div class="autocomplete">
        <ejs-autocomplete
            :dataSource="oilAndGasData"
            :placeholder="waterMark"
        ></ejs-autocomplete>
        <button class="btn">Pesquisar</button>
    </div>
</template>

<script>
import { AutoCompleteComponent as EjsAutocomplete } from "@syncfusion/ej2-vue-dropdowns";
export default {
    data() {
        const waterMark = "Pesquise aqui...";
        const oilAndGasData = [
            "Exploração Offshore",
            "Plataforma de Petróleo",
            "Gasoduto Submarino",
            "Refinaria de Petróleo",
            "Sonda de Perfuração",
            "Exploração Terrestre",
            "Produção de Gás Natural",
            "Reservatórios de Petróleo",
            "Gasolina",
            "Petróleo Bruto",
            "LNG (Gás Natural Liquefeito)",
        ];

        return {
            waterMark,
            oilAndGasData,
        };
    },
    components: {
        "ejs-autocomplete": EjsAutocomplete,
    },
};
</script>

<style scoped>
.autocomplete {
    width: 100%;
    margin-right: 10px;
    padding: 0 10px;
    justify-content: space-between;
    align-items: ;
    display: flex;
}
.btn {
    width: 100%;
    max-width: 100px;
    height: 100%;
    margin-left: 10px;
    border: 1px solid #ff0046;
}
.btn:hover {
    background-color: #ff0046;
    color: #fff;
}
</style>
