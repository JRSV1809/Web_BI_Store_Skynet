/*
 * Project: System Temp
 * Description : JS to managment of User Managment View
 */
(function($){
    var UserManagment = {
        init: function(){
            let table = new DataTable('#table_users');
        },
        initModalSaveUser: function(){
            UserManagment.listenerFiledModalAddUser()
            $('#name').val('')
            $('#username').val('')
            $('#email').val('')
            $('#password').val('')
        },
        listenerFiledModalAddUser: function(){
            $('#name, #username, #email, #password ').unbind().on('keydown keyup change', function () {
                let name = $('#name').val()
                let username = $('#username').val()
                let email = $('#email').val()
                let password = $('#password').val()
                if (name.length > 0 && username.length > 0 && email.length > 0 && password.length > 0) {
                    $('.btn-save-user').removeClass('disabled')
                } else {
                    $('.btn-save-user').addClass('disabled')
                }
            })
        },
        saveUser: function(){
            let name = $('#name').val()
            let username = $('#username').val()
            let email = $('#email').val()
            let password = $('#password').val()

            let payload = {
                'option': 'save_user',
                'name': name,
                'username': username,
                'email': email,
                'password': password
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
                            title: "Usuario Registrado",
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
        },
        deleteUser: function(id){
            let payload = {
                'option': 'delete_user',
                'id': id
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
                            title: "Usuario Eliminado",
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
        },
        initModaResetPassword: function(id){
            $('#password-reset').val('')
            $('#user_id').val(id)
            $('#password-reset').unbind().on('keydown keyup change', function () {
                let password = $('#password-reset').val()
                if (password.length > 0) {
                    $('.btn-password-user').removeClass('disabled')
                } else {
                    $('.btn-password-user').addClass('disabled')
                }
            })
        },
        resetPassword: function(){
            let password = $('#password-reset').val()
            let user_id = $('#user_id').val()
            let payload = {
                'option': 'reset_password',
                'password': password,
                'id':user_id
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
                            title: "Contraseña Actualizada",
                            icon: "success",
                            confirmButtonText: "Ok",
                            allowOutsideClick : false,
                            allowEscapeKey: false
                        }).then(() => {
                        });  
                    }
                }).fail(function (e) {
                    console.log(e);
                });
            });
        }
    }
    
    $(document).ready(function(){
        UserManagment.init();
    })
    
    window.UserManagment = UserManagment;
})(jQuery)
