function openModalHeader(mod_name) {
  var modal = document.getElementById(mod_name);


  // Add open class to make visible and trigger animation
  modal.classList.add('open');
}

function closeModalHeader(mod_name) {
  if ($("#H-chat-content").css("display") == "flex"){
    swapChatListHeader()
  } 
  else{
    var modal = document.getElementById(mod_name);
    

    modal.classList.remove('open');
  }
}

var chatPk;

function  swapChatListHeader(){
  if ($("#H-chat-content").css("display") == "flex"){
    $("#H-chat-content").css("display", "none");
    $("#H-chats-header").css("display", "flex");
    $("#H-chats").css("display", "flex");
  }
    
  else if ($("#H-chat-content").css("display") == "none"){
    $("#H-chat-content").css("display", "flex");
    $("#H-chats-header").css("display", "none");
    $("#H-chats").css("display", "none");
  }
}

$(".H-chat").on("click", function () {
  swapChatListHeader();
  let ChatExPk = $(this).find("input").val();
  let filePk = $("#file-pk").val();
  loadChatHeader(null, filePk, ChatExPk);
})




function getMessagesHeader () {
  $.ajax({
    url:$("#get-messages").val(),
    method: 'get',
    data: {
      chatPk: chatPk,
    },
    success: function(data){
      $("#H-chat-messages").empty()
      messagesContainer = $("#H-chat-messages")
      for (let key in data.messages) {
        
        if (data.users_pks[0] === data.messages[key].user_id){
          let messageHtml =`<div class="message-container">
                              <div class="H-user-icon"><img src="${data.users[0]}" alt="Your profile picture" class="H-your-logo"></div>
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
                            <div class="H-user-icon"><img src="${data.users[1]}" alt="Your profile picture" class="H-your-logo"></div>
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






function loadChatHeader(fileOwnerPk, filePk, ChatExPk=null) {
  console.log(filePk)
  $.ajax({
    url:$("#create-chat").val(),
    method: 'get',
    data: {
      ChatExPk: ChatExPk,
      fileOwnerPk: fileOwnerPk,
      filePk: filePk,
    },
    success: function(data){
      chatPk = data.chat_pk;
      $("#chat-pk").val(data.chat_pk)
      $("#H-chat-name").html(data.chat_name)
    },
    complete: getMessagesHeader,
  });
  
}

$("#H-send-button").on("click", function(){
  let message = $("#H-message-input").val()
  if (message === ''){

  }
  else{
    $("#H-message-input").val('')
    messagesContainer = $("#H-chat-messages")
    messagesContainer.animate({ scrollTop: messagesContainer.prop("scrollHeight")}, 1000);
    $.ajax({
      url:$("#create-message").val(),
      method: 'get',
      data: {
        messageContent: message,
        chatPk: chatPk,
      },
      success: function(data){
          if (data.is_uploader === true){
          var messageHtml =`<div class="message-container right"><div class="H-user-icon"><img src="${data.user_image}" alt="Your profile picture" class="H-your-logo"></div><div class="message-cloud right"><img src="/static/images/bubble_point.svg" alt="Bubble Point" class="point right"><div class="message-box"><span class="message-text">${data.message}</span></div></div></div>`
        }
        else{
          var messageHtml =`<div class="message-container"><div class="H-user-icon"><img src="${data.user_image}" alt="Your profile picture" class="H-your-logo"></div><div class="message-cloud"><img src="/static/images/bubble_point.svg" alt="Bubble Point" class="point"><div class="message-box"><span class="message-text">${data.message}</span></div></div></div>`
        }
        messagesContainer.append(messageHtml);;
      }
    })
    }
  
})
