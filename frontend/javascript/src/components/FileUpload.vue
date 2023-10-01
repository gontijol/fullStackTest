<template>
    <div class="container-full">
        <img alt="Ouronova" class="logo" src="@/../../../img/image.png" />
        <div class="row">
            <div class="col-md-6">
                <h2 class="font-weight-bold">Load File</h2>
                <div class="file-upload-container" @click="selectFile">
                    <div class="file-icons">
                        <div
                            class="file-icon"
                            v-for="type in supportedFileTypes"
                            :key="type"
                        >
                            <i class="fa" :class="fileTypeIcons[type]"></i>
                            <span>{{ type }}</span>
                        </div>
                    </div>

                    <input
                        type="file"
                        ref="fileInput"
                        style="display: none"
                        @change="handleFileChange"
                    />
                    <p v-if="selectedFileName">{{ selectedFileName }}</p>
                    <p v-else>Drag and drop or click to select a file</p>
                </div>
            </div>
            <div class="col-md-6">
                <h2 class="font-weight-bold">Load From The Web</h2>
                <div class="data-type-buttons">
                    <button
                        v-for="type in supportedFileTypes"
                        :key="type"
                        class="btn btn-primary"
                        @click="loadFromWeb(type)"
                    >
                        {{ type }}
                    </button>
                </div>
                <div class="form-group">
                    <label for="url">URL:</label>
                    <input
                        type="text"
                        class="form-control"
                        id="url"
                        v-model="webUrl"
                    />
                </div>
                <div class="form-group">
                    <label for="proxy">Proxy (optional):</label>
                    <input
                        type="text"
                        class="form-control"
                        id="proxy"
                        v-model="webProxy"
                    />
                </div>
                <div>
                    <h3>Sample Datasets (Requires access to web)</h3>
                    <!-- Grid de botões de amostras -->
                    <div class="sample-datasets">
                        <button
                            v-for="dataset in sampleDatasets"
                            :key="dataset"
                            class="btn btn-secondary"
                            @click="loadSampleDataset(dataset)"
                        >
                            {{ dataset }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import FileLoader from "@/components/FileLoader.vue"; // Importe o componente FileLoader

export default {
    data() {
        return {
            supportedFileTypes: [".csv", ".tsv", ".xls", ".xlsx", ".PARQUET"],
            fileTypeIcons: {
                ".csv": "fa-file-csv",
                ".tsv": "fa-file-alt",
                ".xls": "fa-file-excel",
                ".xlsx": "fa-file-excel",
                ".PARQUET": "fa-file-archive",
            },
            selectedFileName: "",
            webUrl: "",
            webProxy: "",
            sampleDatasets: [
                "COVID-19",
                "Seinfeld",
                "The Simpsons",
                "Video Games",
                "Movies",
                "makeTimeDataFrame",
            ],
        };
    },
    methods: {
        selectFile() {
            this.$refs.fileInput.click();
        },
        handleFileChange(event) {
            const file = event.target.files[0];
            if (file) {
                this.selectedFileName = file.name;
                // Lógica para carregar o arquivo
            }
        },
        loadFromWeb(type) {
            // Lógica para carregar arquivo da web com tipo especificado
        },
        loadSampleDataset(dataset) {
            // Lógica para carregar amostra de dataset
        },
    },
};
</script>

<style scoped>
/* Estilos personalizados podem ser adicionados aqui */
.file-upload-container {
    border: 2px dashed #ccc;
    padding: 20px;
    cursor: pointer;
    text-align: center;
}

.file-icons {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}
.form-group {
    margin-bottom: 1rem;
    margin-top: 1rem;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.container-full {
    width: 100%;

    box-sizing: border-box;
}
.form-control {
    width: 80%;
}

.file-icon {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.file-icon i {
    font-size: 24px;
    margin-bottom: 5px;
}

.sample-datasets button {
    margin-right: 10px;
    margin-bottom: 10px;
}
.logo {
    display: flex;
    width: 80%;
    margin: 0 auto 1rem;
    justify-content: center;
    align-items: center;
}
</style>
