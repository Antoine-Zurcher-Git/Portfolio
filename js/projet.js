'use strict';

function projet_events(){

    function generer_projets(){
        read_json("resources/jsons/projet.json",generer);
    }

    function generer(data){
        document.querySelector("#projet_section .emplacement_projet").innerHTML = "";
        

        for (let projet of data.projet){

            document.querySelector("#projet_section .emplacement_projet").innerHTML += `
            <div class="unite_projet">
                <div class="projet_titre">
                    <a class="link" href="${projet.lien}" target="_blank">${projet.titre} </a>
                    <p class="projet_date"> - ${projet.date}</p>
                </div>
                <p class="projet_description">${projet.description}</p>
                <div class="projet_illustration">
                    <img class="projet_image" src="${projet.illustration}"/>
                </div>
                
            </div>
            `;

        }


    }


    generer_projets();

}