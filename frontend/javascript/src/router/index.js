import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/Home.vue";
import FileUpload from "@/components/FileUpload.vue";
import SearchBar from "@/components/SearchBar.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView,
        },
        {
            path: "/reference1",
            name: "fileupload",
            component: FileUpload,
        },
        {
            path: "/reference2",
            name: "searchbar",
            component: SearchBar,
        },
    ],
});

export default router;
