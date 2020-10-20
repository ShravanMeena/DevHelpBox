$('#formControlRange').on("input", function() {
      $('.output').val(" £" + this.value + ",000");
      }).trigger("change");