'use strict';

function about_events(){

    function generer_contacts(){
        read_json("resources/jsons/contact.json",generer);
    }

    function generer(data){
        document.querySelector("#about_section .about_contact").innerHTML = "";
        

        for (let contact of data.contacts){
            var clic = "div";
            var cliclass = "inclicable";
            if(contact.clicable){
                clic = "a";
                var cliclass = "";
            }
            document.querySelector("#about_section .about_contact").innerHTML += `
            <button class="contact_button">
            <${clic} href="${contact.lien}" target="_blank" class="unite_contact ${cliclass}">
                
                <div class="contact_logo">
                    <img class="contact_img" src="${contact.logo}" alt="${contact.nom}">
                </div>
                <div class="contact_texte">
                    <span class="contact_span" >${contact.text}</span>
                </div>
                
            </${clic}>
            </button>
            `;

        }


    }


    generer_contacts();

}