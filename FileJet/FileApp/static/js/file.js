function openModal(mod_name) {
  var modal = document.getElementById(mod_name);

  // Add open class to make visible and trigger animation
  modal.classList.add('open');
}

function closeModal(mod_name) {
  if ($("#chat-content").css("display") == "flex"){
    swapChatList()
  } 
  else{
    var modal = document.getElementById(mod_name);
    // Remove open class to hide and trigger animation
    modal.classList.remove('open');
  }
}

var chatPk;

$("#oModal").on("click", loadStandartChat)

function loadStandartChat(){
  let fileOwnerPk = $("#file-owner-pk").val();
  let filePk = $("#file-pk").val();
  
  loadChat(fileOwnerPk, filePk)
}

function  swapChatList(){
  if ($("#chat-content").css("display") == "flex"){
    $("#chat-content").css("display", "none")
    $("#choose-chat-header").css("display", "flex");
    $("#chats").css("display", "flex");
  }
    
  else if ($("#chat-content").css("display") == "none"){
    $("#chat-content").css("display", "flex")
    $("#choose-chat-header").css("display", "none");
    $("#chats").css("display", "none");
  }
}

$(".chat").on("click", function () {
  swapChatList()
  let fileUserPk = $(this).find("input").val();
  let filePk = $("#file-pk").val();
  loadChat(fileUserPk, filePk);
})

function loadChat(fileOwnerPk, filePk) {
  $.ajax({
    url:$("#create-chat").val(),
    method: 'get',
    data: {
      fileOwnerPk: fileOwnerPk,
      filePk: filePk,
    },
    success: function(data){
      chatPk = data.chat_pk;
      $("#chat-pk").val(data.chat_pk)
	    $("#chat-name").html(data.chat_name)
    },
    complete: function (data) {
      $.ajax({
        url:$("#get-messages").val(),
        method: 'get',
        data: {
          chatPk: chatPk,
        },
        success: function(data){
          $("#chat-messages").empty()
          messagesContainer = $("#chat-messages")
          for (let key in data.messages) {
            
            if (data.users_pks[0] === data.messages[key].user_id){
              let messageHtml =`<div class="message-container">
                                  <div class="user-icon"><img src="${data.users[0]}" alt="Your profile picture" class="your-logo"></div>
                                    <div class="message-cloud">
                                      <img src="/static/images/bubble_point.svg" alt="Bubble Point" class="point">
                                      <div class="message-box">
                                        <span class="message-text">
                                        ${data.messages[key].message}
                                        </span>
                                    </div>
                                  </div>
                                </div>`
              messagesContainer.append(messageHtml);
            }

            else if (data.users_pks[1] === data.messages[key].user_id){
              let messageRightHtml =`<div class="message-container right">
                                <div class="user-icon"><img src="${data.users[1]}" alt="Your profile picture" class="your-logo"></div>
                                  <div class="message-cloud right">
                                    <img src="/static/images/bubble_point.svg" alt="Bubble Point" class="point right">
                                    <div class="message-box">
                                      <span class="message-text">
                                      ${data.messages[key].message}
                                      </span>
                                  </div>
                                </div>
                              </div>`
              messagesContainer.append(messageRightHtml);
            }
            
          };
        }
      });
    }
  });
  
}

$("#send-button").on("click", function(){
  let message = $("#message-input").val()
  $("#message-input").val('')
  messagesContainer = $("#chat-messages")
  messagesContainer.animate({ scrollTop: messagesContainer.prop("scrollHeight")}, 1000);
  $.ajax({
    url:$("#create-message").val(),
    method: 'get',
    data: {
      messageContent: message,
      chatPk: chatPk,
    },
    success: function(data){
	    let messageHtml =`<div class="message-container"><div class="user-icon"><img src="${data.user_image}" alt="Your profile picture" class="your-logo"></div><div class="message-cloud"><img src="/static/images/bubble_point.svg" alt="Bubble Point" class="point"><div class="message-box"><span class="message-text">${data.message}</span></div></div></div>`
      messagesContainer.append(messageHtml);;
    }
  })
})
