<template>
    <div class="container-full">
        <img alt="Ouronova" class="logo" src="@/../../../img/image.png" />
        <div class="body-container">
            <div>
                <h2 class="font-weight-bold">Load File</h2>

                <div v-if="selectedFileName != ''" class="custom-progress">
                    <div
                        class="progress-bar"
                        :style="{ width: progressBarWidth }"
                    ></div>
                </div>

                <div
                    v-if="!fileLoaded"
                    class="draggable-container"
                    @dragover.prevent
                    @drop="drop"
                >
                    <slot>
                        <div class="file-upload-container" @click="selectFile">
                            <div class="file-icons">
                                <div
                                    class="file-icon"
                                    v-for="type in supportedFileTypesExtensions"
                                    :key="type"
                                >
                                    <div class="arquivo-outline">
                                        <i :class="fileTypeIcons[type]"></i>
                                        <span class="file-names">{{
                                            type
                                        }}</span>
                                    </div>
                                </div>
                            </div>

                            <input
                                type="file"
                                ref="fileInput"
                                style="display: none"
                                @change="handleFileChange"
                            />
                            <p v-if="selectedFileName">
                                {{ selectedFileName }}
                            </p>
                            <p v-else>
                                Drag and drop or click to select a file
                            </p>
                        </div>
                    </slot>
                </div>
            </div>

            <div>
                <h2 class="font-weight-bold">Load From The Web</h2>

                <div class="data-type-buttons">
                    Data Type:
                    <button
                        v-for="type in supportedFileTypes"
                        :key="type"
                        class="btn"
                        style="margin: 5px 5px 5px 5px"
                        :class="{
                            'btn-danger': type === selectedWebType,
                            'btn-secondary': type !== selectedWebType,
                        }"
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

                <span class="sample-dataset">Sample Dataset</span>
                <span> (Requires access to web)</span>

                <!-- Grid de botões de amostras -->
                <div class="sample-datasets">
                    <button
                        v-for="dataset in sampleDatasets"
                        :key="dataset"
                        class="btn btn-secondary"
                        style="margin: 5px 5px 5px 5px"
                        @click="loadSampleDataset(dataset)"
                        :class="{
                            'btn-danger': dataset === selectedSampleDataset,
                            'btn-secondary': dataset !== selectedSampleDataset,
                        }"
                    >
                        {{ dataset }}
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            progressBarWidth: "0%",
            supportedFileTypes: ["CSV", "TSV", "JSON", "EXCEL", "PARQUET"],
            supportedFileTypesExtensions: [
                ".csv",
                ".tsv",
                ".xls",
                ".xlsx",
                ".PARQUET",
            ],

            fileTypeIcons: {
                ".csv": "fa-file-csv",
                ".tsv": "fa-file-alt",
                ".xls": "fa-file-excel",
                ".xlsx": "fa-file-excel",
                ".PARQUET": "fa-file-alt",
            },
            fileLoaded: false,
            selectedFileName: "",
            selectedWebType: "",
            selectedSampleDataset: "",
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
    watch: {
        selectedFileName(newValue) {
            if (newValue !== "") {
                this.startLoading();
            }
        },
    },
    methods: {
        handleFileChange(event) {
            const file = event.target.files[0];
            if (file) {
                const fileType = `.${file.name.split(".").pop()}`;
                if (this.supportedFileTypesExtensions.includes(fileType)) {
                    this.selectedFileName = file.name;
                    // Lógica para carregar o arquivo
                } else {
                    // O tipo de arquivo não é suportado, você pode exibir uma mensagem de erro ou rejeitar o arquivo.
                    alert("Tipo de arquivo não suportado.");
                    // Limpar o valor do input de arquivo
                    this.$refs.fileInput.value = "";
                }
            }
        },
        drop(event) {
            // Impede o comportamento padrão do navegador para evitar que o arquivo seja aberto no navegador
            event.preventDefault();

            // Obtém a lista de arquivos soltos
            const files = event.dataTransfer.files;

            // Faça algo com os arquivos soltos, como carregá-los ou processá-los
            for (let i = 0; i < files.length; i++) {
                if (this.files != 0) {
                    const fileType = `.${files[0].name.split(".").pop()}`;
                    if (this.supportedFileTypesExtensions.includes(fileType)) {
                        this.startLoading();
                        this.selectedFileName = files[0].name;

                        // Lógica para carregar o arquivo
                    } else {
                        // O tipo de arquivo não é suportado, você pode exibir uma mensagem de erro ou rejeitar o arquivo.
                        alert("Tipo de arquivo não suportado.");
                        // Limpar o valor do input de arquivo
                        this.$refs.fileInput.value = "";
                    }
                }
            }
        },

        selectFile() {
            this.$refs.fileInput.click();
        },
        startLoading() {
            this.fileLoaded = true;
            for (let i = 0; i <= 100; i++) {
                setTimeout(() => {
                    this.progressBarWidth = `${i}%`;
                }, i * 20);
            }
            setTimeout(() => {
                this.fileLoaded = false;
            }, 2000);
        },

        loadFromWeb(type) {
            this.selectedWebType = type;
        },

        loadSampleDataset(dataset) {
            this.selectedSampleDataset = dataset;
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
.arquivo-outline {
    width: 40px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #7d7d7d;
}
.container-full {
    width: 100%;
    box-sizing: border-box;
    padding-left: 15px;
    padding-right: 15px;
}
.sample-dataset {
    font-size: 18px;
    font-weight: bold;
    border-radius: 4px;
    display: inline-block;
    align-items: center;
    margin-bottom: 10px;
}
@media (max-width: 1023px) {
    .btn {
        width: 30%;
    }
}
.form-control {
    width: 80%;
    border-radius: 4px;
    border: 1px solid #7d7d7d;
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
    padding: 0.3rem 2rem;
    display: inline-block;
    border-radius: 4px;
    align-items: center;
    height: 40px;
}

.sample-datasets {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    width: 100%;
    margin-bottom: 20px;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 10px;
}
@media (max-width: 1023px) {
    .sample-datasets button {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
        flex-direction: column;
    }

    .sample-datasets {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
        flex-direction: column;
    }
}
.file-names {
    font-size: 14px;
    color: #ffffff;
    background-color: #000000;
    border-radius: 4px;
    padding: 2px 2px;
    display: inline-block;
    align-items: center;
}
.logo {
    display: flex;
    width: 50%;
    margin: 0 auto 1rem;
    justify-content: center;
    align-items: center;
}
.btn-1 {
    background-color: #000000;
    color: #ffffff;
    border: 1px solid #000000;
}
.btn-2 {
    background-color: #ffffff;
    color: #000000;
    border: 1px solid #000000;
}
.custom-progress {
    height: 30px;
    width: 100%;
    border: 1px solid #ccc;
    padding: 3px;
    border-radius: 4px;
    margin: 10px 0;
    position: relative;
    overflow: hidden; /* Adicione overflow: hidden para esconder a parte da barra de progresso fora da div */
}

.progress-bar {
    height: 100%;
    background-color: #ff0046;
    transition: width 2s ease-in-out; /* Adicione a transição à propriedade width */
}
</style>
