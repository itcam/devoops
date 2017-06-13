var oTable;
var TableDatatablesButtons = function () {
    var initTable3 = function () {
        var table = $('#sample_3');
        // oTable开始
        oTable = table.dataTable({
            "processing": true,
            "serverSide": true,
            "ajax": {
                    "type":"POST",
                    "url":"/server/get/",
                    "dataSrc":function(data){
                        return data.data;
                     }
            },
             "createdRow": function( row, data, dataIndex ) {
                    $('td', row).eq(0).attr('style', 'text-align: center;');
            },

            "columns":[
                        {"data":"id","sWidth":"5.1%","orderable":false},
                        {"data":"HOSTNAME","orderable":false,"sDefaultContent" : "","sWidth" : "",
                        "render" : function(data, type, full, meta) {
                                data ="<a style='font-weight:bold' data-id="+full.id+"><font color='blue'>"+data+"</font></a>";
                        return   data;
                        }},
                        {"data":"IPADDR",
                        "render" : function(data, type, full, meta) {
                                data ="<a style='font-weight:bold' data-id="+full.id+"><font color='blue'>"+data+"</font></a>";
                        return   data;
                        }},
                        {"data":"APPLICATION"},
                        {"data":"DATABASE"},
                        {"data":"PROJECT"},
                        {"data":"ADD_TIME"},
                        {
            "data": "id",
             "sWidth" : "15%",
                        "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                $(nTd).html("<a href='javascript:void(0);' " +
                "onclick='_editFun(\"" + oData.id + "\",\"" + oData.HOSTNAME + "\",\"" + oData.IPADDR + "\",\"" + oData.APPLICATION + "\",\"" + oData.DATABASE + "\",\"" + oData.PROJECT + "\",\"" + oData.ADD_TIME + "\")' class=\'btn btn-primary\' >编辑</a>&nbsp;&nbsp;")
                    .append("<a href='javascript:void(0);' onclick='_deleteFun(" + sData + ")' class=\'btn btn-danger\' style=\'align-content: right\'>删除</a>");
            }
                        },
//                         {
//                             "mData" : "id",
//                             "orderable" : false, // 禁用排序
//                             "sDefaultContent" : '',
//                             "sWidth" : "15%",
//                             "render":function(data, type, row, meta){
//                             return  data='<button id="editOne" class="btn btn-success btn-sm"  data-id='+data+' data-hostname='+oTable.data()+'>编 辑</button><button id="deleteOne" class="btn btn-danger btn-sm" data-id='+data+'>删 除</button>';
//                                 // var html = '<a href="javascript:void(0);" class="delete btn btn-default btn-xs"><i class="fa fa-times"></i> 删除</a>'
//                                 // return html
//                         }},
//                         {
//                             "mData" : "id",
//                             "orderable" : false, // 禁用排序
//                             "sDefaultContent" : '',
//                             "sWidth" : "10%",
//                             "render":function(data, type, full, meta){
//                             return  data='<button id="deleteOne" class="btn btn-danger btn-sm" data-id='+data+'>删 除</button>';
//                         }}
                    ],
            "columnDefs" :
            [{
                "orderable" : false, // 禁用排序
                "targets" : [0], // 指定的列
                "data" : "id",
                "render" : function(data, type, full, meta) {
                // return '<input type="checkbox" value="'+ data + '" name="id"/>';
                    return '<label class="mt-checkbox mt-checkbox-single mt-checkbox-outline"><input type="checkbox" class="checkboxes" value="1" /><span></span></label>';
                }
            }],

            "language": {
                "aria": {
                    "sortAscending": ": activate to sort column ascending",
                    "sortDescending": ": activate to sort column descending"
                },
                "emptyTable": "没有数据",
                "info": "Showing _START_ to _END_ of _TOTAL_ entries",
                "infoEmpty": "No entries found",
                "infoFiltered": "(filtered1 from _MAX_ total entries)",
                "lengthMenu": "_MENU_ entries",
                "search": "搜索:",
                "zeroRecords": "No matching records found"
            },
            buttons: [
                { extend: 'print', className: 'btn dark btn-outline' },
                { extend: 'copy', className: 'btn red btn-outline' },
                { extend: 'pdf', className: 'btn green btn-outline' },
                { extend: 'excel', className: 'btn yellow btn-outline ' },
                { extend: 'csv', className: 'btn purple btn-outline ' },
                { extend: 'colvis', className: 'btn dark btn-outline', text: 'Columns'}
            ],

            // setup responsive extension: http://datatables.net/extensions/responsive/
            responsive: true,

            //"ordering": false, disable column ordering 
            //"paging": false, disable pagination

            "order": [
                [0, false]
            ],
            
            "lengthMenu": [
                [5, 10, 15, 20, -1],
                [5, 10, 15, 20, "All"] // change per page values here
            ],
            // set the initial value
            "pageLength": 5,

            "fnInitComplete": function (oSettings, json) {
        $('<a href="#myModal" id="addFun" class="btn btn-primary" data-toggle="modal">新增</a>' + '&nbsp;' +
        '<a href="#" class="btn btn-primary" id="editFun">修改</a> ' + '&nbsp;' +
        '<a href="#" class="btn btn-danger" id="deleteFun">删除</a>' + '&nbsp;').appendTo($('.myBtnBox'));
//         $("#deleteFun").click(_deleteList);
//         $("#editFun").click(_value);
//         $("#addFun").click(_init);
        }
        });

        // oTable结束

        // $(document).delegate('#deleteOne','click',function() {
        // var id=$(this).data("id");
        // $("#delSubmit").val(id);
        // $("#deleteOneModal").modal('show');
        // });
        //
        // $(document).delegate('#editOne','click',function() {
        // var id=$(this).data("id");
        // var hostname=$(this).data("hostname");
        //     console.log($(this).data());
        // $("#hostname").val(hostname);
        // $("#editSubmit").val(id);
        // $("#editOrderStatus").modal('show');
        // });
        //
        // $(document).delegate('#delSubmit','click',function(){
        // var id=$(this).val();
        // $('#deleteOneModal').modal('hide');
        // $.ajax({
        //     url:"/server/delete/",
        //     data: { id: id},
        //     async:true,
        //     type:"POST",
        //     dataType:"json",
        //     cache:false,    //不允许缓存
        //     success: function(data){
        //         var obj = eval(data);
        //         if(obj.status==0)
        //         {
        //             // window.location.reload();
        //             oTable.api().ajax.reload(null,false);
        //             // oTable.fnReloadAjax(oTable.fnSettings());
        //         }
        //         else
        //         {
        //             alert("删除失败");
        //         }
        //
        //     },
        //     error:function(data){
        //         alert("请求异常");
        //     }
        //     });
        // });
        // $(document).delegate('#editSubmit','click',function(){
        // var id=$(this).val();
        // $('#deleteOneModal').modal('hide');
        // $.ajax({
        //     url:"/server/update/",
        //     data: { id: id},
        //     async:true,
        //     type:"POST",
        //     dataType:"json",
        //     cache:false,    //不允许缓存
        //     success: function(data){
        //         var obj = eval(data);
        //         if(obj.status==0)
        //         {
        //             // window.location.reload();
        //             oTable.api().ajax.reload(null,false);
        //             // oTable.fnReloadAjax(oTable.fnSettings());
        //         }
        //         else
        //         {
        //             alert("删除失败");
        //         }
        //
        //     },
        //     error:function(data){
        //         alert("请求异常");
        //     }
        //     });
        // });


        // handle datatable custom tools
        $('#sample_3_tools > li > a.tool-action').on('click', function() {
            var action = $(this).attr('data-action');
            oTable.DataTable().button(action).trigger();
        });
    }
    var initAjaxDatatables = function () {
        //init date pickers
        $('.date-picker').datepicker({
            rtl: App.isRTL(),
            autoclose: true
        });
        var grid = new Datatable();
        grid.init({
            src: $("#datatable_ajax"),
            onSuccess: function (grid, response) {
                // grid:        grid object
                // response:    json object of server side ajax response
                // execute some code after table records loaded
            },
            onError: function (grid) {
                // execute some code on network or other general error  
            },
            onDataLoad: function(grid) {
                // execute some code on ajax data load
            },
            loadingMessage: 'Loading...',
            dataTable: { // here you can define a typical datatable settings from http://datatables.net/usage/options 

                // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
                // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/scripts/datatable.js). 
                // So when dropdowns used the scrollable div should be removed. 
                
                //"dom": "<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'<'table-group-actions pull-right'>>r>t<'row'<'col-md-8 col-sm-12'pli><'col-md-4 col-sm-12'>>",
                
                "bStateSave": true, // save datatable state(pagination, sort, etc) in cookie.

                "lengthMenu": [
                    [10, 20, 50, 100, 150, -1],
                    [10, 20, 50, 100, 150, "All"] // change per page values here
                ],
                "pageLength": 10, // default record count per page
                "ajax": {
                    "url": "../demo/table_ajax.php", // ajax source
                },
                "order": [
                    [1, "asc"]
                ],// set first column as a default sort by asc
            
                // Or you can use remote translation file
                //"language": {
                //   url: '//cdn.datatables.net/plug-ins/3cfcc339e89/i18n/Portuguese.json'
                //},

                buttons: [
                    { extend: 'print', className: 'btn default' },
                    { extend: 'copy', className: 'btn default' },
                    { extend: 'pdf', className: 'btn default' },
                    { extend: 'excel', className: 'btn default' },
                    { extend: 'csv', className: 'btn default' },
                    {
                        text: 'Reload',
                        className: 'btn default',
                        action: function ( e, dt, node, config ) {
                            dt.ajax.reload();
                            alert('Datatable reloaded!');
                        }
                    }
                ],

            }
        });

        // handle group actionsubmit button click
        grid.getTableWrapper().on('click', '.table-group-action-submit', function (e) {
            e.preventDefault();
            var action = $(".table-group-action-input", grid.getTableWrapper());
            if (action.val() != "" && grid.getSelectedRowsCount() > 0) {
                grid.setAjaxParam("customActionType", "group_action");
                grid.setAjaxParam("customActionName", action.val());
                grid.setAjaxParam("id", grid.getSelectedRows());
                grid.getDataTable().ajax.reload();
                grid.clearAjaxParams();
            } else if (action.val() == "") {
                App.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: 'Please select an action',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
            } else if (grid.getSelectedRowsCount() === 0) {
                App.alert({
                    type: 'danger',
                    icon: 'warning',
                    message: 'No record selected',
                    container: grid.getTableWrapper(),
                    place: 'prepend'
                });
            }
        });

        //grid.setAjaxParam("customActionType", "group_action");
        //grid.getDataTable().ajax.reload();
        //grid.clearAjaxParams();

        // handle datatable custom tools
        // $('#datatable_ajax_tools > li > a.tool-action').on('click', function() {
        //     var action = $(this).attr('data-action');
        //     grid.getDataTable().button(action).trigger();
        // });
    }

    return {

        //main function to initiate the module
        init: function () {

            if (!jQuery().dataTable) {
                return;
            }

            // initTable1();
            // initTable2();
            initTable3();
            $("#btnEdit").click(_editFunAjax);
            initAjaxDatatables();
        }

    };

}();

jQuery(document).ready(function() {
    TableDatatablesButtons.init();
});

function _editFun(id, hostname, ipaddr, app,database,project,add_time) {
    $("#objectId").val(id);
    $("#hostname").val(hostname);
    $("#ipaddr").val(ipaddr);
    $("#appname").val(app);
    $("#database").val(database);
    $("#pro_name").val(project);
    $("#add_time").val(add_time);
    $("#editOrderStatus").modal("show");
}

function _editFunAjax() {
var id = $("#objectId").val();
var hostname = $("#hostname").val();
var ipaddr = $("#ipaddr").val();
var appname = $("#appname").val();
var database = $("#database").val();
var pro_name = $("#pro_name").val();
var add_time = $("#add_time").val();
var jsonData = {
    "id": id,
    "hostname": hostname,
    "ipaddr": ipaddr,
    "appname": appname,
    "database":database,
    "pro_name":pro_name,
    "add_time":add_time
};
    console.log(jsonData);
$.ajax({
    type: 'POST',
    url: '/server/update/',
    data: jsonData,
    success: function (json) {
        if (json.status==0) {
            oTable.api().ajax.reload(null,false);
            $("#editOrderStatus").modal("hide");
        } else {
            alert("更新失败");
        }
    }
});
}