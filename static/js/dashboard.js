/*
 * Project: System Temp
 * Description : JS to managment of Dashboard Page
 */
(function($){
    var Dashboard = {
        init: function(){
            
        },
        getModalProjection: function() {
            $("#uploadFileProjection-body").empty()
            let payload = {
                'option': 'get_url_upload_file'
            }
            
            Pace.track(function() {
                $.ajax({
                    method: "POST",
                    data: JSON.stringify(payload),
                    contentType: "application/json",
                    dataType: 'json',
                }).done(function(data) {
                    if (data.error_fg) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: data.error_msg,
                        })
                    } else {
                        $("#uploadFileProjection-body").append(`
                            <input type="text" value="${data.data_name}" class="form-control text-black d-none" id="filename">
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <label>Nombre</label>
                                        <input type="text" placeholder="Nombre" class="form-control text-black" id="name_projection">
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-lg-12">
                                        <div class="form-group">
                                            <label>Archivo</label>
                                            <form class="dropzone" id="my-great-dropzone"></form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `)
                        var file_upload = false
        
                        let dropzoneOptions = {
                            url: data.data, 
                            method: 'put',
                            maxFiles: 1, 
                            addRemoveLinks: true,
                            headers: {
                                'Content-Type': 'application/octet-stream'
                            },
                            success: function(file, response) {
                                file_upload = true
                                Swal.fire({
                                    icon: 'success',
                                    title: 'Éxito',
                                    text: 'Archivo subido correctamente',
                                });
                                if (name_projection.length > 0) {
                                    $('.btn-upload-projection').removeClass('disabled')
                                } else {
                                    $('.btn-upload-projection').addClass('disabled')
                                }
                            },
                            error: function(file, errorMessage) {
                                Swal.fire({
                                    icon: 'error',
                                    title: 'Error',
                                    text: 'No se pudo subir el archivo',
                                });
                            }
                        };

                        let myDropzone = new Dropzone("#my-great-dropzone", dropzoneOptions);

                        $('#name_projection').unbind().on('keydown keyup change', function () {
                            let name_projection = $('#name_projection').val()
                            if (name_projection.length > 0 && file_upload == true) {
                                $('.btn-upload-projection').removeClass('disabled')
                            } else {
                                $('.btn-upload-projection').addClass('disabled')
                            }
                        })
                    }
                }).fail(function(e) {
                    console.log(e);
                });
            });
        },
        saveProjection: function(){
            let name_projection = $('#name_projection').val()
            let name_file = $('#filename').val()
            let payload = {
                'option': 'save_projection',
                'name': name_projection,
                'file': name_file
            }

            Pace.track(function () {
                $.ajax({
                    method: "POST",
                    data: JSON.stringify(payload),
                    contentType: "application/json",
                    dataType: 'json',
                }).done(function (data) {
                    if (data.error_fg) {
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: data.error_msg,
                        })
                    } else {
                        Swal.fire({
                            title: "Datos de Proyeccion Guardado",
                            icon: "success",
                            confirmButtonText: "Ok",
                            allowOutsideClick : false,
                            allowEscapeKey: false
                        }).then(() => {
                            location.reload()
                          });
                    }
                }).fail(function (e) {
                    console.log(e);
                });
            });
        }
    }
    
    $(document).ready(function(){
        Dashboard.init();
    })
    
    window.Dashboard = Dashboard;
})(jQuery)
