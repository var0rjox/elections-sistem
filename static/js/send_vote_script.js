const btn_vote = document.getElementById("btn-vote");

btn_vote.addEventListener("click", () => {
  let radios = document.getElementsByName("selected_candidate");
  let is_any_radio_selected = false;
  let selected_candidate = "";

  // Check if any radio button is selected
  for (let i = 0; i < radios.length && !is_any_radio_selected; i++) {
    if (radios[i].checked) {
      is_any_radio_selected = true;
      selected_candidate = radios[i].dataset.candidateName;
    }
  }

  let modal_body_message = "";
  let modal_buttons = "";

  if (!is_any_radio_selected) {
    modal_body_message = "Seleccione un candidato";
    modal_buttons = `<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Aceptar</button>`;
  } else {
    modal_body_message = `¿Esta seguro de seleccionar a <b>${selected_candidate}</b> para votar?`;
    modal_buttons = `
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button id="btn-submit" type="button" class="btn btn-primary">Enviar</button>
        `;
  }

  document.getElementById("content-modal-body").innerHTML = modal_body_message;
  document.getElementById("content-modal-footer").innerHTML = modal_buttons;

  // Show modal
  var myModal = new bootstrap.Modal(document.getElementById("modal_alert"));
  myModal.show();

  // Second modal
  document.getElementById("btn-submit").addEventListener("click", () => {
    myModal.hide();
    
    let secondModalBody =
    "Haz finalizado el proceso para emitir tu voto, Gracias";

    document.getElementById("btn-close-modal").style.display = "none";
    document.getElementById("content-modal-body").innerHTML = secondModalBody;
    document.getElementById("content-modal-footer").style.display = "none";
    
    var secondModal = new bootstrap.Modal(
      document.getElementById("modal_alert")
      );
    document.querySelector("form").submit();
    secondModal.show();

    setTimeout(() => {
      secondModal.hide();
    }, 5000);
  });
});

document.addEventListener("DOMContentLoaded", () => {
  var candidateCards = document.querySelectorAll(".card-candidate");

  candidateCards.forEach((card) => {
    card.addEventListener("click", () => {
      var candidateId = card.getAttribute("data-candidate");
      document.getElementById(candidateId).checked = true;
    });
  });
});

function selectCandidate(selectedDiv) {
  var cards = document.getElementsByClassName("bg-body-secondary");
  for (var i = 0; i < cards.length; i++) {
    cards[i].classList.remove("bg-body-secondary");
  }
  selectedDiv.classList.add("bg-body-secondary");
  selectedDiv.querySelector("input").checked = true;
}
