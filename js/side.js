'use strict';

function side_events(){

    function generer_contacts_side(){
        read_json("resources/jsons/contact.json",generer);
    }

    function generer(data){
        document.querySelector(".emplacement_contact_side").innerHTML = "";
        

        for (let contact of data.contacts){
            var clic = "div";
            var cliclass = "inclicable";
            if(contact.clicable){
                clic = "a";
                var cliclass = "";
            }
            document.querySelector(".emplacement_contact_side").innerHTML += `

            <li><${clic} href="${contact.lien}" class="unite_contact_side ${cliclass}">
                <div class="contact_side_logo">
                    <img class="contact_side_img" src="${contact.logo}" alt="${contact.nom}">
                </div>
                
            </${clic}></li>
            `;

            // <div class="contact_side_texte">
            //         <span class="contact_side_span" >${contact.text}</span>
            //     </div>

        }


    }


    generer_contacts_side();

}