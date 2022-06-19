
        'use strict';

        $(document).ready(function(){
        
            $('input#id_search').quicksearch('table tbody tr');
        
            $('.indc-item').click( function() {
                let item = $(this).attr('num');
                
                if( $(this).is( ':checked' ) ){ 
                    $('#card').load('vue/valcard.php?item='+item); 
                }
         
            });
        
            $('table').on('click','.itemindc', function() {
                let item = $(this).attr('num');
                $('#lstindc').load('vue/lstindc.php?item='+item);
         
            });
        
            $('#graphe2, #tabviz').click( function() { 
                let indc = '';
                let couv = '';
                let tps = '';
        
                $(".indc-item:checked").each( function() {
                    indc = indc + '-'+ $(this).attr('num');
                });
        
                $(".pole-item:checked").each( function() {
                    couv = couv + '-'+ $(this).attr('num');
                });
        
                let deb = $('#tpsdeb').val();
                let fin = $('#tpsfin').val();
        
                if (indc!='') {
                    $('#card').load('vue/tablelst.php?indc='+indc+'&pole='+couv+'&deb='+deb+'&fin='+fin);
                }else{
                    alert('Vous devez sÃ©lectionner au-moins un indicateur.');
                }
         
            });
        
        
            $('#graphe1').click( function() { 
                let indc = '';
                let fillcard = new Array();
                let indctab = new Array();
                let a = 0;
                $('#card').html('<center>Patientez SVP ...</center>');
                $(".indc-item:checked").each( function() {
                    indc = $(this).attr('num');
        
                    if (indc!='') {
                        if (a==0) {
                            $('#card').load('vue/valcard.php?item='+indc);
                        }else{ $('#card'+a).load('vue/valcard.php?item='+indc); }
                        a = a + 1;
                    }
        
                });
         
            });
        
        
        
            $('.section_15').on('change','#itemstc', function() {
                let item = $(this).val();
                $('#lstindc').load('vue/tabledatas.php?item='+item);
         
            });
        
        
        });