function bytesToSize(bytes) {
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB']
  if (bytes === 0) return 'n/a'
  const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)), 10)
  if (i === 0) return `${bytes} ${sizes[i]})`
  return `${(bytes / (1024 ** i)).toFixed(1)} ${sizes[i]}`
}

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
const form = document.querySelector('#form');
const paragraphs = form.querySelectorAll('p');
FileInputTag.addEventListener('change', () => {
  if (FileInputTag.files && FileInputTag.files[0]) {
    paragraphs.forEach((paragraph) => {
      paragraph = $(paragraph)
      paragraph.css("display", "flex");
    });
    $("#id_file_path").closest("p").css("display", "none")
    $(".send").css("display", "flex")
    $("#id_private").closest("p").append("Зробити приватним!");
    const reader = new FileReader();
    var FileWholeName = $('input[type=file]').val().replace(/C:\\fakepath\\/i, '');
    var FileName = FileWholeName.split(".").slice(0, -1).join(".");
    var FileType = FileWholeName.split('.').pop();
    var FileSize = FileInputTag.files[0].size;
    FileSize = bytesToSize(FileSize)

    $("#file-category").val(FileType)

    FileNameTag.innerHTML = FileName;
    FileTypeTag.innerHTML = FileType;
    FileSizeTag.innerHTML = FileSize;
    $(".image_design").css("display", "flex");
    $("#without-text").css("display", "none");
  }
})