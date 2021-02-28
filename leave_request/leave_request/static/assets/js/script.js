$(document).ready(function(){

    //login & signup btn
    $('[btn_attr]').click(function(){
        var conn = $(this).attr('btn_attr');
        $('[popup_attr="'+conn+'"]').addClass('open-dropdown');
        $('.main-overlay').show();
    });
    $('.main-overlay').click(function(){
        $('[popup_attr').removeClass('open-dropdown');
        $(this).hide();
    });
    $('.login-btn').click(function(){
        $('.tap-form a[href="#login_tap"]').tab('show');
    });
    $('.sign-btn').click(function(){
        $('.tap-form a[href="#sign_tap"]').tab('show');
    });

    //dropdown
    $('[btn_drop]').click(function(){
        var conn = $(this).attr('btn_drop');
        $('[ul_drop="'+conn+'"]').toggleClass('open-dropdown');
    });
    $(document).click(function(e){
        if( $(e.target).closest('[btn_drop] , [ul_drop]').length > 0 ) {
            if( $(e.target).closest('.delete-dropdown').length > 0 ) {
                $('[ul_drop]').removeClass('open-dropdown');
            }
        }
        else{
            $('[ul_drop]').removeClass('open-dropdown');
        }
    });
    $('.sort-ul .sort-li').click(function(){
        var conn = $(this).parents('.sort-ul').attr('ul_drop');
        $('.sort-p[btn_drop="'+conn+'"]').text($(this).text());
        $(this).parents('.sort-ul').removeClass('open-dropdown');
    });

    //open menu
    $('.menu-bar').click(function(){
        $('.aside-content').addClass('open-menu');
        $('.main-overlay').show();
    });
    $('.main-overlay').click(function(){
        $('.aside-content').removeClass('open-menu');
    });
    $('.filter-checkbox input').change(function(){
        $('.main-overlay').hide();
        $('.aside-content').removeClass('open-menu');
    });


    //chat
    $('.user-chat').click(function(){
        $('.first-screen').hide();
        $('.sec-screen').show();
        $('.sec-screen .chat-body').scrollTop($('.sec-screen .main-messages').prop('scrollHeight'));
    });
    $('.back-chat').click(function(){
        $('.first-screen').show();
        $('.sec-screen').hide();
    });


    //dropify plugin
    $('.dropify').dropify();
    $('.dropify-wrapper .dropify-message p').html('Upload your image <span> Drag & drop or browse your image here </span>');
    $('.dropify-wrapper .dropify-message p.dropify-error').text('لقد حدث خطا');
    $('.dropify-wrapper .dropify-message span.file-icon').html('<i class="fas fa-camera"></i>');

    //plugin select2
    $('.default-select').select2({ minimumResultsForSearch: -1});


    //slider bar
    $('.example').createSlide({
        output:'.num-subscribers',
        maxvalue: 10
    });

    $('.feature-group .feature-h').click(function(){
        $('.feature-group .feature-form').toggleClass('d-flex');
    });

    
    $('.equ-result').on( ' keyup' , function(){
        var price =$('#price').val();
        var num_subscribers = $('#num-subscribers').val();
        var result ;
        if(price == ''){
            $('#Payout').val('');
        }else{
            result = parseInt(price) * parseInt(num_subscribers)  * .7 ;
            $('#Payout').val(result);
        }
    });

});