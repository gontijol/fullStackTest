<template>
    <div class="file-loader">
        <div class="progress-bar" :style="{ width: progress + '%' }"></div>
        <div class="progress-text">{{ progress }}%</div>
    </div>
</template>

<script>
export default {
    props: {
        progress: Number, // A porcentagem de progresso do carregamento (passada como prop)
    },
};
</script>

<style scoped>
/* Estilos personalizados do componente de progresso */
.file-loader {
    width: 100%;
    background-color: #f0f0f0;
    border-radius: 4px;
    height: 30px;
    margin-top: 10px;
}

.progress-bar {
    height: 100%;
    background-color: #007bff;
    border-radius: 4px;
    transition: width 0.3s;
}

.progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-weight: bold;
}
</style>
