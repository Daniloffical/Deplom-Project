// $("#id_image").on( "change", function() {
//     console.log($(this))
//     if ($(this).files && $(this).files[0]) {
//         console.log($(this))
//         let reader = new FileReader();

//         reader.onload = function (event) {
//             $('#image-file').attr('src', event.target.result);
//         }

//         reader.readAsDataURL($(this).files[0]);
// }
// })

const imgInput = document.querySelector('#id_image')
const imgEl = document.querySelector('#image-file')
imgInput.addEventListener('change', () => {
  if (imgInput.files && imgInput.files[0]) {
    const reader = new FileReader();
    reader.onload = (e) => {
      imgEl.src = e.target.result;
    }
    reader.readAsDataURL(imgInput.files[0]);
  }
})

const FileInputTag = document.querySelector('#id_file_path');
const FileNameTag = document.querySelector('#file-name');
const FileTypeTag = document.querySelector('#file-type');
const FileSizeTag = document.querySelector('#file-size');
FileInputTag.addEventListener('change', () => {
  if (FileInputTag.files && FileInputTag.files[0]) {
    const reader = new FileReader();
    var FileWholeName = $('input[type=file]').val().replace(/C:\\fakepath\\/i, '');
    var FileName = FileWholeName.split(".").slice(0, -1).join(".");
    var FileType = FileWholeName.split('.').pop();
    var FileSize = FileInputTag.files[0].size;
    FileNameTag.innerHTML = FileName;
    FileTypeTag.innerHTML = FileType;
    FileSizeTag.innerHTML = FileSize;
    $(".image_design").css("display", "flex");
    $("#without-text").css("display", "none");
  }
})